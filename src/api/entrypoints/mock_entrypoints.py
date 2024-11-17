from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends

from api.tools import routes
from config import app_config, json_config
from interfaces import base_factory, base_use_case
from tools.di_containers import repositories_di_container, use_cases_di_container

router = APIRouter(tags=["mock"])

app_config = app_config.app_config
json_config = json_config.json_config


@router.get("/{rest_of_path:path}")
@inject
async def mock_get(
    rest_of_path: str,
    get_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.get_use_case]
    ),
    repository_factory: base_factory.BaseFactory = Depends(
        Provide[repositories_di_container.RepositoriesContainer.json_db_repository_factory]
    ),
) -> dict | list:
    """
    Получить данные из ресурса по переданному url-маршруту
    :param rest_of_path: url-маршрут
    :param get_use_case: use case для get-запроса
    :param repository_factory: фабрика репозиториев
    :return: данные из ресурса
    """

    path_data = routes.get_route_with_http_get(rest_of_path)

    if not path_data:
        raise ValueError("URL-путь не был найден")

    resource = path_data.actual_path[0]
    repository = repository_factory.create(json_config.json_db_path, resource)

    return get_use_case(path_data, repository, resource)


@router.post("/{rest_of_path:path}")
@inject
async def mock_post(
    rest_of_path: str,
    new_data: dict | list[dict | list] = Body(...),
    post_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.post_use_case]
    ),
    get_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.get_use_case]
    ),
    repository_factory: base_factory.BaseFactory = Depends(
        Provide[repositories_di_container.RepositoriesContainer.json_db_repository_factory]
    ),
) -> dict | list:
    """
    Добавить данные в ресурс по переданному url-маршруту
    :param rest_of_path: url-маршрут
    :param new_data: новые данные для ресурса
    :param post_use_case: use case для post-запроса
    :param get_use_case: use case для get-запроса
    :param repository_factory: фабрика репозиториев
    :return: данные из ресурса
    """

    path_data = routes.get_route_with_http_post(rest_of_path)

    if not path_data:
        raise ValueError("URL-путь не был найден")

    resource = path_data.actual_path[0]
    repository = repository_factory.create(json_config.json_db_path, resource)

    result = post_use_case(
        path_data.json_path, path_data.actual_path, repository, resource, new_data
    )

    if path_data.return_path and path_data.actual_return_path:
        resource = path_data.actual_return_path[0]

        return get_use_case(
            path_data.return_path, path_data.actual_return_path, repository, resource
        )

    return result


@router.put("/{rest_of_path:path}")
@inject
async def mock_put(
    rest_of_path: str,
    new_data: dict = Body(...),
    put_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.put_use_case]
    ),
    get_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.get_use_case]
    ),
    repository_factory: base_factory.BaseFactory = Depends(
        Provide[repositories_di_container.RepositoriesContainer.json_db_repository_factory]
    ),
) -> dict | list:
    """
    Обновить данные из ресурса по переданному url-маршруту
    :param rest_of_path: url-маршрут
    :param new_data: новые данные для ресурса
    :param put_use_case: use case для put-запроса
    :param get_use_case: use case для get-запроса
    :param repository_factory: фабрика репозиториев
    :return: данные из ресурса
    """

    path_data = routes.get_route_with_http_put(rest_of_path)

    if not path_data:
        raise ValueError("URL-путь не был найден")

    resource = path_data.actual_path[0]
    repository = repository_factory.create(json_config.json_db_path, resource)

    result = put_use_case(path_data, repository, resource, new_data)

    if path_data.return_path and path_data.actual_return_path:
        resource = path_data.actual_return_path[0]

        return get_use_case(
            path_data.return_path, path_data.actual_return_path, repository, resource
        )

    return result


@router.patch("/{rest_of_path:path}")
@inject
async def mock_patch(
    rest_of_path: str,
    new_data: dict = Body(...),
    patch_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.patch_use_case]
    ),
    get_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.get_use_case]
    ),
    repository_factory: base_factory.BaseFactory = Depends(
        Provide[repositories_di_container.RepositoriesContainer.json_db_repository_factory]
    ),
) -> dict | list:
    """
    Обновить данные из ресурса по переданному url-маршруту
    :param rest_of_path: url-маршрут
    :param new_data: новые данные для ресурса
    :param patch_use_case: use case для patch-запроса
    :param get_use_case: use case для get-запроса
    :param repository_factory: фабрика репозиториев
    :return: данные из ресурса
    """

    path_data = routes.get_route_with_http_patch(rest_of_path)

    if not path_data:
        raise ValueError("URL-путь не был найден")

    resource = path_data.actual_path[0]
    repository = repository_factory.create(json_config.json_db_path, resource)

    result = patch_use_case(path_data, repository, resource, new_data)

    if path_data.return_path and path_data.actual_return_path:
        resource = path_data.actual_return_path[0]

        return get_use_case(
            path_data.return_path, path_data.actual_return_path, repository, resource
        )

    return result


@router.delete("/{rest_of_path:path}")
@inject
async def mock_delete(
    rest_of_path: str,
    delete_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.delete_use_case]
    ),
    get_use_case: base_use_case.UseCase = Depends(
        Provide[use_cases_di_container.UseCasesContainer.get_use_case]
    ),
    repository_factory: base_factory.BaseFactory = Depends(
        Provide[repositories_di_container.RepositoriesContainer.json_db_repository_factory]
    ),
) -> dict | list | None:
    """
    Удалить данные из ресурса по переданному url-маршруту
    :param rest_of_path: url-маршрут
    :param delete_use_case: use case для patch-запроса
    :param get_use_case: use case для get-запроса
    :param repository_factory: фабрика репозиториев
    :return: данные из ресурса
    """

    path_data = routes.get_route_with_http_delete(rest_of_path)

    if not path_data:
        raise ValueError("URL-путь не был найден")

    resource = path_data.actual_path[0]
    repository = repository_factory.create(json_config.json_db_path, resource)

    result = delete_use_case(path_data, repository, resource)

    if path_data.return_path and path_data.actual_return_path:
        resource = path_data.actual_return_path[0]

        return get_use_case(
            path_data.return_path, path_data.actual_return_path, repository, resource
        )

    return result
