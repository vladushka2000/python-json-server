import dataclasses

from config import json_config
from interfaces import base_repository, base_use_case
from models.dto import routes_dto

config = json_config.json_config


class BaseHTTPUseCase(base_use_case.UseCase):
    """
    Базовый класс для HTTP Use-кейсов
    """

    @dataclasses.dataclass
    class _ResourceFilterDTO:
        """
        DTO, содержащий данные по ресурсу и фильтре по одному из его полей
        """

        resource: str
        field: str | None = None
        value: any = None

    def _create_filters(
        self, json_path: list[str], actual_path: list[str]
    ) -> list[_ResourceFilterDTO]:
        """
        Создать фильтры для ресурса
        :param json_path: маршрут из json
        :param actual_path: маршрут, введенный пользователем
        :return: фильтры для поиска ресурса
        """

        filters = []

        for index in range(len(actual_path)):
            is_resource = actual_path[index] == json_path[index]

            if not is_resource:
                filters[-1].field = json_path[index].lstrip(":")
                filters[-1].value = actual_path[index]

                continue

            filters.append(self._ResourceFilterDTO(resource=actual_path[index]))

        return filters

    def _find_first_appearance(
        self, values: list[dict], field: str, target_value: any
    ) -> list | dict:
        """
        Найти первое появление объекта в списке по значению его поля
        :param values: список объектовв, среди которых проводится поиск
        :param field: название поля объекта
        :param target_value: целевое значение поля объекта
        :return: объект, удовлетворяющий условиям
        """

        for value in values:
            if field in value:
                value_type = type(value[field])
            else:
                continue

            if value[field] == value_type(target_value):
                return value

    def _get_data(
        self,
        repository: base_repository.BaseRepository,
        resource: str,
        filters: list[_ResourceFilterDTO],
    ) -> dict | list:
        """
        Получить данные ресурса
        :param repository: объект репозитория
        :param resource: название ресурса
        :param filters: список фильтров для поиска данных ресурса
        :return: данные ресурса
        """

        result = {resource: repository.retrieve()}

        for filter_ in filters:
            result = result[filter_.resource]

            if filter_.field:
                result = self._find_first_appearance(result, filter_.field, filter_.value)

        return result

    def _execute_repository_logic(
        self,
        repository: base_repository.BaseRepository,
        data: dict | list[dict | list],
        new_data: dict | list[dict | list] | None,
    ) -> dict | list[dict | list] | None:
        """
        Выполнить логику репозитория
        :param repository: объект репозитория
        :param data: данные
        :param new_data: новые данные для ресурса
        :return: результат выполнения логики репозитория
        """

        raise NotImplementedError

    def __call__(
        self,
        paths: routes_dto.RoutesMapDTO,
        repository: base_repository.BaseRepository,
        resource: str,
        new_data: dict | list[dict | list] = None,
    ) -> dict | list[dict | list] | None:
        """
        Выполнить логику Use-кейса
        :param paths: ресурсы, переданные пользователем
        :param repository: объект репозитория
        :param resource: название ресурса
        :param new_data: новые данные для ресурса
        :return: результат выполнения логики репозитория
        """

        filters = self._create_filters(paths.json_path, paths.actual_path)

        data = self._get_data(repository, resource, filters)

        return self._execute_repository_logic(repository, data, new_data)


class GETUseCase(BaseHTTPUseCase):
    """
    Класс Use-кейса для метода GET
    """

    def _execute_repository_logic(
        self,
        repository: base_repository.BaseRepository,
        data: dict | list[dict | list],
        new_data: dict | list[dict | list] | None,
    ) -> dict | list | None:
        """
        Получить данные ресурса
        :param repository: объект репозитория
        :param data: данные
        :param new_data: новые данные для ресурса
        :return: данные ресурса
        """

        return data


class POSTUseCase(BaseHTTPUseCase):
    """
    Класс Use-кейса для метода POST
    """

    def _execute_repository_logic(
        self,
        repository: base_repository.BaseRepository,
        data: dict | list[dict | list],
        new_data: dict | list[dict | list],
    ) -> dict | list | None:
        """
        Добавить данные в ресурс
        :param repository: объект репозитория
        :param data: данные
        :param new_data: новые данные для ресурса
        :return: результат работы репозитория
        """

        repository.create(data, new_data)
        repository.persist()

        return


class PUTUseCase(BaseHTTPUseCase):
    """
    Класс Use-кейса для метода PUT
    """

    def _execute_repository_logic(
        self,
        repository: base_repository.BaseRepository,
        data: dict | list[dict | list],
        new_data: dict | list[dict | list],
    ) -> dict | list | None:
        """
        Обновить данные ресурса
        :param repository: объект репозитория
        :param data: данные
        :param new_data: новые данные для ресурса
        :return: результат работы репозитория
        """

        repository.update(data, new_data)
        repository.persist()

        return


class PATCHUseCase(BaseHTTPUseCase):
    """
    Класс Use-кейса для метода PATCH
    """

    def _execute_repository_logic(
        self,
        repository: base_repository.BaseRepository,
        data: dict | list[dict | list],
        new_data: dict | list[dict | list],
    ) -> dict | list | None:
        """
        Обновить данные ресурса
        :param repository: объект репозитория
        :param data: данные
        :param new_data: новые данные для ресурса
        :return: результат работы репозитория
        """

        repository.update(data, new_data, True)
        repository.persist()

        return


class DELETEUseCase(BaseHTTPUseCase):
    """
    Класс Use-кейса для метода DELETE
    """

    def _execute_repository_logic(
        self,
        repository: base_repository.BaseRepository,
        data: dict | list[dict | list],
        new_data: dict | list[dict | list],
    ) -> dict | list | None:
        """
        Удалить данные ресурса
        :param repository: объект репозитория
        :param data: данные
        :param new_data: новые данные для ресурса
        :return: результат работы репозитория
        """

        repository.delete(data)
        repository.persist()

        return
