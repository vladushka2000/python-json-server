import pathlib

from interfaces import base_factory
from repositories import json_db_repository, json_routes_repository


class JSONDBRepositoryFactory(base_factory.BaseFactory):
    """
    Фабрика репозитория для json-БД
    """

    def create(self, json_path: pathlib.Path, resource: str) -> json_db_repository.JSONDBRepository:
        """
        Создать объект репозитория json-БД
        :param json_path: путь до json-файла
        :param resource: название ресурса
        :return: объект репозитория json-БД
        """

        return json_db_repository.JSONDBRepository(json_path, resource)


class JSONRoutesRepositoryFactory(base_factory.BaseFactory):
    """
    Фабрика репозитория для json-конфигурации маршрутизации
    """

    def create(self, json_path: pathlib.Path) -> json_routes_repository.JSONRoutesRepository:
        """
        Создать объект репозитория json-БД
        :param json_path: путь до json-файла
        :return: объект репозитория json-БД
        """

        return json_routes_repository.JSONRoutesRepository(json_path)
