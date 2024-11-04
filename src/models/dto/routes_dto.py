from pydantic import Field

from interfaces import base_dto


class JSONParsedRoutesDTO(base_dto.BaseDTO):
    """
    DTO, распаршенный из JSON и содержащий доступный маршрут и его Regex
    """

    path: str = Field(description="URL-путь")
    regex: str = Field(description="Regex-строка на основе url-пути")


class RoutesMapDTO(base_dto.BaseDTO):
    """
    DTO, содержащий доступный маршрут из JSON и ввод пользователя
    """

    json_path: list[str] = Field(description="URL-путь из JSON")
    actual_path: list[str] = Field(description="URL-путь из запроса пользователя")
