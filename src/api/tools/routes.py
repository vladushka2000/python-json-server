import re

from models.dto import routes_dto
from use_cases import json_route_use_case

routes: dict | None = None


def get_routes() -> None:
    """
    Получить маршруты из JSON
    """

    global routes

    use_case = json_route_use_case.JSONRoutesDataKeeperUseCase()
    routes = use_case()


def _get_route(rest_of_path: str, routes_from_json: dict) -> routes_dto.RoutesMapDTO | None:
    """
    Получить объект url-маршрута
    :param rest_of_path: переданный url пользователя
    :param routes_from_json: url из json
    :return: объект url-маршрута
    """

    for route in routes_from_json:
        if re.fullmatch(route.regex, rest_of_path):
            return_path = route.return_path.split("/") if route.return_path else None
            actual_return_path = (
                route.actual_return_path.split("/") if route.actual_return_path else None
            )

            if return_path and not actual_return_path:
                raise ValueError(
                    "Не задан маршрут до ресурса из которого будет возвращаться значение"
                )

            return routes_dto.RoutesMapDTO(
                json_path=route.path.split("/"),
                actual_path=rest_of_path.split("/"),
                return_path=return_path,
                actual_return_path=actual_return_path,
            )

    return None


def get_route_with_http_get(rest_of_path: str) -> routes_dto.RoutesMapDTO | None:
    """
    Получить объект url-маршрута из get-запроса
    :param rest_of_path: переданный url пользователя
    :return: объект url-маршрута
    """

    if routes is None:
        raise ValueError("Url-маршруты не были получены из JSON")

    return _get_route(rest_of_path, routes["GET"])


def get_route_with_http_post(rest_of_path: str) -> routes_dto.RoutesMapDTO | None:
    """
    Получить объект url-маршрута из post-запроса
    :param rest_of_path: переданный url пользователя
    :return: объект url-маршрута
    """

    if routes is None:
        raise ValueError("Url-маршруты не были получены из JSON")

    return _get_route(rest_of_path, routes["POST"])


def get_route_with_http_put(rest_of_path: str) -> routes_dto.RoutesMapDTO | None:
    """
    Получить объект url-маршрута из put-запроса
    :param rest_of_path: переданный url пользователя
    :return: объект url-маршрута
    """

    if routes is None:
        raise ValueError("Url-маршруты не были получены из JSON")

    return _get_route(rest_of_path, routes["PUT"])


def get_route_with_http_patch(rest_of_path: str) -> routes_dto.RoutesMapDTO | None:
    """
    Получить объект url-маршрута из patch-запроса
    :param rest_of_path: переданный url пользователя
    :return: объект url-маршрута
    """

    if routes is None:
        raise ValueError("Url-маршруты не были получены из JSON")

    return _get_route(rest_of_path, routes["PATCH"])


def get_route_with_http_delete(rest_of_path: str) -> routes_dto.RoutesMapDTO | None:
    """
    Получить объект url-маршрута из delete-запроса
    :param rest_of_path: переданный url пользователя
    :return: объект url-маршрута
    """

    if routes is None:
        raise ValueError("Url-маршруты не были получены из JSON")

    return _get_route(rest_of_path, routes["DELETE"])
