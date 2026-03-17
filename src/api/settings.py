from dataclasses import dataclass, field
from os import environ as env

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, slots=True)
class Settings:
    DEBUG: bool = field(default=env["DEBUG"] == "true")
    APP_DATABASE_DSN: str = field(default=env["APP_DATABASE_DSN"])
    LOGS_DATABASE_DSN: str = field(default=env["LOGS_DATABASE_DSN"])
