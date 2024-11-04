from dependency_injector import containers, providers

from tools.factories import repositories_factory


class RepositoriesContainer(containers.DeclarativeContainer):
    """
    DI-контейнер с провайдерами репозиториев
    """

    wiring_config = containers.WiringConfiguration(
        modules=["use_cases.json_route_use_case", "api.entrypoints.mock_entrypoints"]
    )

    json_db_repository_factory = providers.Factory(repositories_factory.JSONDBRepositoryFactory)
    json_routes_repository_factory = providers.Factory(
        repositories_factory.JSONRoutesRepositoryFactory
    )
