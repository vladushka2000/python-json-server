import enum


class HTTPMethodEnum(enum.Enum):
    """
    Enum, содержащий доступные HTTP-методы
    """

    GET = "GET"
    POST = "POST"
    UPDATE = "UPDATE"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"
