from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_name: str = "ElectrolyzerAPI"
    api_version: str = "v1"
    # Add more configuration settings as needed


settings = Settings()
