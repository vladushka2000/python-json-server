class BaseKeeper:
    """
    Базовый класс для сохранения объектов на время жизни приложения
    """

    def __init__(self, object_: any) -> None:
        """
        Инициализировать переменные
        :param object_: объект для сохранения
        """

        self._object = object_

    def get(self) -> any:
        """
        Получить объект
        :return: сохраненный объект
        """

        return self._object
