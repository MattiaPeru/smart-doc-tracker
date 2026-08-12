[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Position = 0)]
    [ValidateSet("Install", "Uninstall")]
    [string]$Operation = "Install",

    [ValidatePattern("^([01]\d|2[0-3]):[0-5]\d$")]
    [string]$CheckTime = "09:00",

    [ValidateRange(0, 3650)]
    [int]$DaysThreshold = 30
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$taskName = "SmartDocTracker-ExpirationCheck"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$pythonPath = Join-Path $projectRoot ".venv\Scripts\python.exe"
$mainScript = Join-Path $projectRoot "src\main.py"

if ($Operation -eq "Uninstall") {
    $existingTask = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
    if ($null -eq $existingTask) {
        Write-Output "Scheduled task '$taskName' is not installed."
        exit 0
    }

    if ($PSCmdlet.ShouldProcess($taskName, "Unregister scheduled task")) {
        Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
        Write-Output "Scheduled task '$taskName' was removed."
    }
    exit 0
}

if (-not (Test-Path -LiteralPath $pythonPath -PathType Leaf)) {
    throw "The project virtual environment was not found. Create .venv and install requirements first."
}
if (-not (Test-Path -LiteralPath $mainScript -PathType Leaf)) {
    throw "The Smart Doc Tracker entry point was not found."
}

$parsedTime = [DateTime]::ParseExact(
    $CheckTime,
    "HH:mm",
    [Globalization.CultureInfo]::InvariantCulture
)
$dailyStart = [DateTime]::Today.Add($parsedTime.TimeOfDay)
$taskArguments = '"{0}" --check-expirations --days-threshold {1}' -f `
    $mainScript, $DaysThreshold

$taskAction = New-ScheduledTaskAction `
    -Execute $pythonPath `
    -Argument $taskArguments `
    -WorkingDirectory $projectRoot
$trigger = New-ScheduledTaskTrigger -Daily -At $dailyStart
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -WakeToRun `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit ([TimeSpan]::FromMinutes(10))
$currentUser = [Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal `
    -UserId $currentUser `
    -LogonType Interactive `
    -RunLevel Limited
$scheduledTask = New-ScheduledTask `
    -Action $taskAction `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal

if ($PSCmdlet.ShouldProcess($taskName, "Register daily expiration check")) {
    Register-ScheduledTask `
        -TaskName $taskName `
        -InputObject $scheduledTask `
        -Force | Out-Null
    Write-Output (
        "Scheduled task '{0}' was installed for {1} with a daily check at {2}." -f `
            $taskName, $currentUser, $CheckTime
    )
}
