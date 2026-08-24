[CmdletBinding()]
param(
    [ValidateRange(0, 3650)]
    [int]$DaysThreshold = 30,

    [ValidateRange(10, 600)]
    [int]$DockerTimeoutSeconds = 120,

    [ValidateRange(10, 300)]
    [int]$MongoTimeoutSeconds = 60,

    [ValidatePattern("^[A-Za-z][A-Za-z0-9_+.-]*$")]
    [string]$OcrLanguage = "eng"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$pythonPath = Join-Path $projectRoot ".venv\Scripts\python.exe"
$composeFile = Join-Path $projectRoot "docker-compose.yml"

function Resolve-DockerCli {
    $dockerCommand = Get-Command "docker.exe" -ErrorAction SilentlyContinue
    if ($null -ne $dockerCommand) {
        return $dockerCommand.Source
    }

    $defaultCliPath = Join-Path `
        $env:ProgramFiles `
        "Docker\Docker\resources\bin\docker.exe"
    if (Test-Path -LiteralPath $defaultCliPath -PathType Leaf) {
        return $defaultCliPath
    }

    throw "Docker CLI was not found. Install Docker Desktop before running the expiration check."
}

function Test-DockerDaemon {
    param([Parameter(Mandatory = $true)][string]$DockerCli)

    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "SilentlyContinue"
        & $DockerCli info --format "{{.ServerVersion}}" *> $null
        $probeSucceeded = $LASTEXITCODE -eq 0
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    return $probeSucceeded
}

function Start-DockerDaemon {
    param(
        [Parameter(Mandatory = $true)][string]$DockerCli,
        [Parameter(Mandatory = $true)][int]$TimeoutSeconds
    )

    if (Test-DockerDaemon -DockerCli $DockerCli) {
        return
    }

    $dockerDesktopPath = Join-Path `
        $env:ProgramFiles `
        "Docker\Docker\Docker Desktop.exe"
    if (-not (Test-Path -LiteralPath $dockerDesktopPath -PathType Leaf)) {
        throw "Docker Desktop could not be started because its executable was not found."
    }

    $desktopProcess = Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue
    if ($null -eq $desktopProcess) {
        Start-Process -FilePath $dockerDesktopPath -WindowStyle Hidden
    }

    $deadline = [DateTime]::UtcNow.AddSeconds($TimeoutSeconds)
    while ([DateTime]::UtcNow -lt $deadline) {
        Start-Sleep -Seconds 2
        if (Test-DockerDaemon -DockerCli $DockerCli) {
            return
        }
    }

    throw "Docker Desktop did not become ready before the local timeout."
}

function Start-MongoService {
    param(
        [Parameter(Mandatory = $true)][string]$DockerCli,
        [Parameter(Mandatory = $true)][int]$TimeoutSeconds
    )

    & $DockerCli compose `
        --file $composeFile `
        --project-directory $projectRoot `
        up -d --pull never mongodb
    if ($LASTEXITCODE -ne 0) {
        throw "The local MongoDB container could not be started."
    }

    $deadline = [DateTime]::UtcNow.AddSeconds($TimeoutSeconds)
    while ([DateTime]::UtcNow -lt $deadline) {
        $previousErrorActionPreference = $ErrorActionPreference
        try {
            $ErrorActionPreference = "SilentlyContinue"
            & $DockerCli compose `
                --file $composeFile `
                --project-directory $projectRoot `
                exec -T mongodb `
                mongosh --quiet --eval "quit(db.adminCommand('ping').ok ? 0 : 1)" `
                *> $null
            $mongoIsReady = $LASTEXITCODE -eq 0
        }
        finally {
            $ErrorActionPreference = $previousErrorActionPreference
        }
        if ($mongoIsReady) {
            return
        }
        Start-Sleep -Seconds 2
    }

    throw "The local MongoDB service did not become ready before the local timeout."
}

if (-not (Test-Path -LiteralPath $pythonPath -PathType Leaf)) {
    throw "The project virtual environment was not found. Create .venv and install requirements first."
}
if (-not (Test-Path -LiteralPath $composeFile -PathType Leaf)) {
    throw "The local Docker Compose configuration was not found."
}

$dockerCli = Resolve-DockerCli
Start-DockerDaemon -DockerCli $dockerCli -TimeoutSeconds $DockerTimeoutSeconds
Start-MongoService -DockerCli $dockerCli -TimeoutSeconds $MongoTimeoutSeconds

& $pythonPath -m smart_doc_tracker `
    --days-threshold $DaysThreshold `
    --language $OcrLanguage
exit $LASTEXITCODE
