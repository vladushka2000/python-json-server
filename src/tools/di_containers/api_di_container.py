import fastapi
from dependency_injector import containers, providers


class APIContainer(containers.DeclarativeContainer):
    """
    DI-контейнер с провайдерами модулей API
    """

    wiring_config = containers.WiringConfiguration(modules=["tools.app_initializer"])

    app = providers.Singleton(fastapi.FastAPI)
