from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BOT_WEBHOOK: AnyHttpUrl

    OPENWEATHER_API_KEY: str
    EXCHANGE_RATES_API_KEY: str

    class Config:
        env_file = 'envs/test.env'
        env_file_encoding = 'utf-8'


settings = Settings()
