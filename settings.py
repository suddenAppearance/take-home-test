from pydantic import BaseSettings, SecretStr
from urllib3.util import Url


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr

    def _get_url(self, scheme: str) -> Url:
        return Url(
            scheme=scheme,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            auth=":".join((self.POSTGRES_USER.get_secret_value(), self.POSTGRES_PASSWORD.get_secret_value())),
            path=self.POSTGRES_DB
        )

    def get_sync_url(self) -> Url:
        return self._get_url("postgresql")

    def get_async_url(self) -> Url:
        return self._get_url("postgresql+asyncpg")


class Settings(BaseSettings):
    SERVICE_NAME: str = "Survey API"
