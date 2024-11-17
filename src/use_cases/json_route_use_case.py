from dependency_injector.wiring import Provide, inject

from config import json_config
from interfaces import base_factory, base_use_case
from models.dto import routes_dto
from tools import regex_tool
from tools.di_containers import repositories_di_container

config = json_config.json_config


class JSONRoutesDataKeeperUseCase(base_use_case.UseCase):
    """
    Use-кейс для сохранения данных маршрутов из JSON
    """

    @inject
    def __call__(
        self,
        repository_factory: base_factory.BaseFactory = Provide[
            repositories_di_container.RepositoriesContainer.json_routes_repository_factory
        ],
    ) -> dict:
        """
        Получить объект Data keeper для маршрутов
        :param repository_factory: фабрика репозиториев
        :return: объект Data keeper для маршрутов
        """

        repository = repository_factory.create(config.json_routes_path)
        routes_map = repository.retrieve()

        for method, routes in routes_map.items():
            routes_map[method] = []

            for route in routes:
                regex_path = regex_tool.RegexTool.create_route_regex(route["url_mask"])
                routes_map[method].append(
                    routes_dto.JSONParsedRoutesDTO(
                        path=route["url_mask"],
                        regex=regex_path,
                        return_path=route["return_mask"],
                        actual_return_path=route["actual_return"],
                    )
                )

        return routes_map
