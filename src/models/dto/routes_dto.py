from pydantic import Field

from interfaces import base_dto


class JSONParsedRoutesDTO(base_dto.BaseDTO):
    """
    DTO, распаршенный из JSON и содержащий доступный маршрут и его Regex
    """

    path: str = Field(description="Маска для URL-пути")
    regex: str = Field(description="Regex-строка на основе маски url-пути")
    return_path: str | None = Field(
        description="Маска URL-пути по которому будет получен ответ от сервера"
    )
    actual_return_path: str | None = Field(description="URL-путь возвращаемого значения")


class RoutesMapDTO(base_dto.BaseDTO):
    """
    DTO, содержащий доступный маршрут из JSON и ввод пользователя
    """

    json_path: list[str] = Field(description="Маска URL-пути из JSON")
    actual_path: list[str] = Field(description="URL-путь из запроса пользователя")
    return_path: list[str] | None = Field(
        description="Маска URL-пути по которому будет получен ответ от сервера"
    )
    actual_return_path: list[str] | None = Field(description="URL-путь возвращаемого значения")
