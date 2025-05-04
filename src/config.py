from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")
    
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_URL: str

    @property
    def db_url(self) -> str:
        return self.DB_URL.format(
            db_user=self.DB_USER,
            db_pass=self.DB_PASS,
            db_host=self.DB_HOST,
            db_port=self.DB_PORT,
            db_name=self.DB_NAME,
        )

def load_settings():
    return Settings()