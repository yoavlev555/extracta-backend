import tomllib
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


def _read_pyproject() -> dict:
    """Read pyproject.toml and return project metadata."""
    pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
    try:
        with pyproject_path.open("rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        return {}


load_dotenv()  # Automatically Load variables from .env directly into Config object
_PYPROJECT = _read_pyproject()  # Read once and cache


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_name: str = _PYPROJECT.get("project", {}).get("name", "extracta-backend")
    version: str = _PYPROJECT.get("project", {}).get("version", "0.0.0-dev")
    debug: bool = False


config = Config()
