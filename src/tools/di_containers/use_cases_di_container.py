from dependency_injector import containers, providers

from use_cases import http_use_case, json_route_use_case


class UseCasesContainer(containers.DeclarativeContainer):
    """
    DI-контейнер с провайдерами Use-кейсов
    """

    wiring_config = containers.WiringConfiguration(modules=["api.entrypoints.mock_entrypoints"])

    json_keeper_use_case = providers.Factory(json_route_use_case.JSONRoutesDataKeeperUseCase)

    get_use_case = providers.Factory(http_use_case.GETUseCase)
    post_use_case = providers.Factory(http_use_case.POSTUseCase)
    put_use_case = providers.Factory(http_use_case.PUTUseCase)
    patch_use_case = providers.Factory(http_use_case.PATCHUseCase)
    delete_use_case = providers.Factory(http_use_case.DELETEUseCase)
