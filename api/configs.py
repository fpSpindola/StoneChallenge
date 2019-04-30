import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class Config:
    current: "Config" = None

    def __init__(self):
        self.LOGS_INDEX_PATTERN = "logs-{month}.{year}"
        self.engine = create_engine(
            f'postgresql+psycopg2://{os.getenv("DB_USER")}:'
            f'{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
        )
        self.engine.connect()
        self.session_factory = sessionmaker(bind=self.engine)

    def create_session(self) -> Session:
        return self.session_factory()

    @classmethod
    def load_from_env(cls) -> "Config":
        load_dotenv(dotenv_path=Path(__file__).parents[1] / ".env")
        Config.current = cls()
        return cls.current


def current_config() -> "Config":
    return Config.current

