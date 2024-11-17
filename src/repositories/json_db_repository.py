import json
import pathlib

from interfaces import base_repository


class JSONDBRepository(base_repository.BaseRepository, base_repository.IsPersistable):
    """
    JSON-репозиторий для базы данных
    """

    def __init__(self, json_path: pathlib.Path, resource: str) -> None:
        """
        Инициализировать переменные
        :param json_path: путь до json-файла
        :param resource: название ресурса
        """

        self._json_path = json_path
        self._resource = resource
        self._json_data: list = self._get_json_data()

    def persist(self) -> None:
        """
        Сохранить изменения в json
        """

        with open(self._json_path, "r+") as file:
            file_data = json.load(file)
            file_data[self._resource] = self._json_data

            file.seek(0)
            file.truncate()

            json.dump(file_data, file, indent=2)

    def _get_json_data(self) -> dict | list:
        with open(self._json_path, "r") as file:
            data = json.load(file)
            result = data[self._resource]

            if not result:
                raise ValueError("Ресурс не был найден в json")

        return result

    def create(self, data_to_append_to: list, data_to_write: dict | list[dict | list]) -> None:
        """
        Добавить данные к ресурсу
        :param data_to_append_to: данные, которые будут дополнены
        :param data_to_write: данные для добавления
        """

        if isinstance(data_to_write, dict):
            data_to_append_to.append(data_to_write)
        else:
            data_to_append_to.extend(data_to_write)

    def retrieve(self) -> list:
        """
        Получить данные из ресурса
        :return: данные из ресурса
        """

        return self._json_data

    def update(self, data_to_update: dict, new_object: dict, is_patch: bool = False) -> dict:
        """
        Обновить данные ресурса
        :param data_to_update: данные, которые будут изменены
        :param new_object: новые данные объекта
        :param is_patch: флаг, объявляющий полное обновление ресурса.
                         True - частичное обновление, False - полное
        """

        if is_patch:
            for key in data_to_update:
                if key in new_object:
                    data_to_update[key] = new_object[key]
        else:
            data_to_update.clear()

            for key, value in new_object.items():
                data_to_update[key] = value

        return data_to_update

    def delete(self, data: dict | list[dict | list]) -> None:
        """
        Удалить данные ресурса
        :param data: данные для удаления
        """

        data.clear()
