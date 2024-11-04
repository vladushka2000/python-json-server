import abc


class UseCase(abc.ABC):
    """
    Базовый класс для Use-кейса
    """

    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> any:
        """
        Выполнить логику кейса
        """

        raise NotImplementedError
