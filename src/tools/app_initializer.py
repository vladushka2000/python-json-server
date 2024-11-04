from fastapi import FastAPI

from api.entrypoints import router_registrator
from api.tools import routes
from tools.di_containers import api_di_container, repositories_di_container, use_cases_di_container


def create_app() -> FastAPI:
    """
    Инициализировать приложение и начальные ресурсы
    :return: приложение FastAPI
    """

    api_container = api_di_container.APIContainer()
    repositories_di_container.RepositoriesContainer()
    use_cases_di_container.UseCasesContainer()

    app = api_container.app()
    router_registrator.register_routers(app)
    routes.get_routes()

    return app
