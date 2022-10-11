from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    class Config(AppSettings.Config):
        pass
