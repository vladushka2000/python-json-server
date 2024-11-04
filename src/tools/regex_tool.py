import re


class RegexTool:
    """
    Утилита для работы с Regex
    """

    @staticmethod
    def create_route_regex(route: str) -> str:
        """
        Создать regex для url-пути
        :param route: url-путь
        :return: regex
        """

        new_route = route
        route_keys = re.findall(r":.[^/]+", new_route)

        for index, key in enumerate(route_keys):
            if index == len(route_keys) - 1 and route.index(key) + len(key) == len(route):
                new_route = new_route.replace(key, "[^/]+")
            else:
                new_route = new_route.replace(key, ".+")

        return new_route
