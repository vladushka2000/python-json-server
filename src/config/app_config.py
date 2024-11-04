import dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Config(BaseSettings):
    """
    Класс настроек для приложения
    """

    app_name: str = Field(description="Название приложения", default="python-json-server")
    app_version: str = Field(description="Версия API", default="v1")

    app_host: str = Field(description="Хост сервиса", default="0.0.0.0")
    app_port: int = Field(description="Порт сервиса", default=7777)


app_config = Config()
