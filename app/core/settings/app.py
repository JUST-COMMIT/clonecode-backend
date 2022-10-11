from typing import Any, Dict
from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    class Config(BaseAppSettings.Config):
        pass

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {}
