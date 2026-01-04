from importlib.metadata import PackageNotFoundError, version

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()  # Automatically Load variables from .env directly into Config object


def _get_version(app_name: str) -> str:
    try:
        return version(app_name)
    except PackageNotFoundError:
        return "0.0.0-dev"


class Config(BaseSettings):
    app_name: str = "extracta-backend"
    debug: bool = False
    version: str = _get_version(app_name)


config = Config()
