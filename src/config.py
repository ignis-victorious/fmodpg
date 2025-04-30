#
#  _________________
#  Import LIBRARIES
from pydantic_settings import BaseSettings, SettingsConfigDict
#  Import FILES
#  _________________


class Settings(BaseSettings):
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()


print(settings.model_dump())
