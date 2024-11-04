from fastapi import FastAPI

from api.entrypoints import index_entrypoint, mock_entrypoints
from config import app_config

app_config = app_config.app_config


def register_routers(app: FastAPI) -> None:
    """
    Зарегистрировать роутеры
    :param app: приложение FastAPI
    """

    app.include_router(index_entrypoint.router, prefix=f"/api/{app_config.app_version}")
    app.include_router(mock_entrypoints.router, prefix=f"/api/{app_config.app_version}")
