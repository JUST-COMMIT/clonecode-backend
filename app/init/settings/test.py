from app.init.settings.app import AppSettings


class TestAppSettings(AppSettings):
    class Config(AppSettings.Config):
        pass
