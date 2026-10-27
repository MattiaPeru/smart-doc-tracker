"""Local settings HTTP endpoints."""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

from ...settings import ReminderSettings, ReminderSettingsError
from ..schemas import ReminderSettingsResponse
from .context import WebRouteContext


def register_settings_routes(context: WebRouteContext) -> APIRouter:
    """Register the settings endpoints with explicit local services."""
    router = APIRouter()
    reminder_settings = context.reminder_settings
    templates = context.templates
    csrf_token = context.csrf_token

    @router.get("/", response_class=HTMLResponse, include_in_schema=False)
    def dashboard(request: Request) -> HTMLResponse:
        """Render the local single-page document dashboard."""
        try:
            default_days = reminder_settings.load().default_notification_days_before
        except ReminderSettingsError:
            default_days = 30
        response = templates.TemplateResponse(
            request=request,
            name="dashboard.html",
            context={
                "alert_days": default_days,
                "csrf_token": csrf_token,
                "max_upload_mb": 25,
            },
        )
        response.headers["Cache-Control"] = "no-store, max-age=0"
        return response

    @router.get("/api/settings/reminders", response_model=ReminderSettingsResponse)
    def get_reminder_settings() -> ReminderSettingsResponse:
        """Return the locally persisted default expiration reminder."""
        try:
            return ReminderSettingsResponse.model_validate(
                reminder_settings.load().model_dump()
            )
        except ReminderSettingsError as exc:
            raise HTTPException(
                status_code=503,
                detail="The local reminder settings are unavailable.",
            ) from exc

    @router.put("/api/settings/reminders", response_model=ReminderSettingsResponse)
    def update_reminder_settings(
        settings: ReminderSettings,
    ) -> ReminderSettingsResponse:
        """Persist the default reminder used by documents without an override."""
        try:
            saved = reminder_settings.save(settings)
            return ReminderSettingsResponse.model_validate(saved.model_dump())
        except ReminderSettingsError as exc:
            raise HTTPException(
                status_code=503,
                detail="The local reminder settings could not be saved.",
            ) from exc

    return router
