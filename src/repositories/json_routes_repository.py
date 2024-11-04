import json
import pathlib

from interfaces import base_repository


class JSONRoutesRepository(base_repository.BaseRepository):
    """
    JSON-репозиторий для настроек маршрутизации
    """

    def __init__(self, json_path: pathlib.Path) -> None:
        """
        Инициализировать переменные
        :param json_path: путь до json-файла
        """

        self._json_path = json_path
        self._json_data: list = self._get_json_data()

    def _get_json_data(self) -> dict | list:
        """
        Получить данные из json
        :return: данные из json
        """

        with open(self._json_path, "r") as file:
            return json.load(file)

    def persist(self, *args, **kwargs) -> any:
        """
        Сохранить изменения
        """

        super().persist(*args, **kwargs)

    def create(self, *args, **kwargs) -> None:
        """
        Добавить данные к ресурсу
        """

        super().create(*args, **kwargs)

    def retrieve(self, *args, **kwargs) -> any:
        """
        Получить данные из ресурса
        """

        return self._json_data

    def update(self, *args, **kwargs) -> None:
        """
        Обновить данные ресурса
        """

        super().update(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        """
        Удалить данные ресурса
        """

        super().update(*args, **kwargs)
