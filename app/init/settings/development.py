from app.init.settings.app import AppSettings


class DevAppSettings(AppSettings):
    class Config(AppSettings.Config):
        pass
