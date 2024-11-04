import abc


class BaseRepository(abc.ABC):
    """
    Базовый класс репозитория
    """

    @abc.abstractmethod
    def persist(self, *args, **kwargs) -> any:
        """
        Сохранить изменения
        """

        raise NotImplementedError

    @abc.abstractmethod
    def create(self, *args, **kwargs) -> any:
        """
        Создать запись
        """

        raise NotImplementedError

    @abc.abstractmethod
    def retrieve(self, *args, **kwargs) -> any:
        """
        Получить запись
        """

        raise NotImplementedError

    @abc.abstractmethod
    def update(self, *args, **kwargs) -> any:
        """
        Обновить запись
        """

        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, *args, **kwargs) -> any:
        """
        Удалить запись
        """

        raise NotImplementedError


class IsPersistable(abc.ABC):
    """
    Класс-миксин для сохранения изменений в репозитории
    """

    @abc.abstractmethod
    def persist(self, *args, **kwargs) -> any:
        """
        Сохранить изменения
        """

        raise NotImplementedError
