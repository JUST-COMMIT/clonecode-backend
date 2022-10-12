from typing import Dict, Type

from app.init.settings.app import AppSettings
from app.init.settings.base import AppEnvTypes, BaseAppSettings
from app.init.settings.development import DevAppSettings
from app.init.settings.production import ProdAppSettings
from app.init.settings.test import TestAppSettings


environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}

def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings.app_env
    config = environments[app_env]
    return config()
