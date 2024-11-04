import pathlib

from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Класс настроек для json-хранилищ
    """

    json_db_path: pathlib.Path = Field(
        description="Путь до json-файла БД",
        default=pathlib.Path.cwd().resolve() / "jsons" / "db.json",
    )
    json_routes_path: pathlib.Path = Field(
        description="Путь до json-файла конфигурации маршрутизации",
        default=pathlib.Path.cwd().resolve() / "jsons" / "routes.json",
    )


json_config = Config()
