from fastapi import Body, APIRouter, HTTPException
from src.model.resource import Resource
from src.data.warehouse import ProcessingMining as pm

router = APIRouter(prefix='/mining')


@router.get('/all-statistic')
def get_all_statistic() -> dict:
    """
    Возвращает всю статистику о выработке ресурсов, содержащуюся в базе
    :return: list
    """
    result = pm.return_all_statistic()

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok', 'statistic': result}


@router.get('/statistic-for-date')
def get_statistic_for_date(date: str) -> dict:
    """
    Возвращает статистику о выработке ресурсов за полученную дату, если такая имеется
    :param date: принимает дату, по которой осуществляется поиск данных о выработке ресурсов
    :return: list
    """
    result = pm.return_statistic_for_date(date)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok', 'statistic': result}


@router.get('/weight-for-category')
def get_weight_for_category(category: str) -> dict:
    """
    Возвращает общее количество ресурса полученной категории которое хранится на складе, с любыми характеристиками, если он имеется
    :param category: принимает название категории (ore, stone, wood....)
    :return: float | bool
    """
    result = pm.return_weight_for_category(category)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok', 'weight': result}


@router.get('/weight-for-params')
def get_weight_for_params(name: str, color: str, grade: str) -> dict:
    """
    Возвращает количество ресурса по строго заданным характеристикам хранящегося на складе, если он имеется
    :param name: название ресурса
    :param color: цвет ресурса
    :param grade: марка ресурса
    :return: float | bool
    """
    result = pm.return_weight_for_params(name, color, grade)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok', 'weight': result}


@router.get('/statistic-for-citizen')
def get_statistic_for_citizen(name: str ) -> dict:
    """
    Возвращает всю выработку горожанина за весь период, согласно полученного имени
    :param name: принимает имя горожанина
    :return: list
    """
    result = pm.return_statistic_for_citizen(name)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok', 'statistic': result}


@router.post('/add-resource')
def add_resource(resource: Resource = Body(embed=True)) -> dict:
    """
    Добавляет Полученные ресурсы на склад и в отдел статистики, суммирует количество добытых ресурсов если идентичные есть на складе,
    Также добавляет данные о ежедневной добыче ресурсов в отдел статистики
    :param resource: принимает сведения о добытых ресурсах за указанную дату
    :return: None
    """
    pm.add_resource_in_warehouse(resource)

    return {'status': 'ok'}


@router.patch('/update-weight')
def update_weight(name: str = Body(embed=True), color: str = Body(embed=True), grade: str = Body(embed=True), weight: float = Body(embed=True)) -> dict:
    """
    Изменяет количество ресурса на складе если идентичные есть на складе, например если часть ресурса уже израсходована
    :param name: название ресурса
    :param color: цвет ресурса
    :param grade: марка ресурса
    :param weight:марка ресурса
    :return: bool
    """
    result = pm.update_weight_resource_in_warehouse(name, color, grade, weight)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok'}


@router.patch('/update-statistic')
def update_statistic(resource: Resource = Body(embed=True)) -> dict:
    """
    Изменяет горожанина, задействованного на добыче определенного ресурса
    :param resource: принимает сведения о добытых ресурсах за указанную дату
    :return: dict
    """
    result = pm.update_citizen_in_statistic(resource)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok'}


@router.patch('/del-statistic')
def del_data_statistic(resource: Resource = Body(embed=True)) -> dict:
    """
    Удаляет из отдела статистики записи о добыче ресурсов, идентичные полученным
    :param resource: принимает сведения о добытых ресурсах за указанную дату
    :return: bool
    """
    result = pm.del_data_statistic(resource)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok'}


@router.patch('/del-data')
def del_data_in_warehouse(name: str = Body(embed=True), color: str = Body(embed=True), grade: str = Body(embed=True)) -> dict:
    """
     Удаляет запись о наличии определенного ресурса со склада
    :param name: название ресурса
    :param color: цвет ресурса
    :param grade: марка ресурса
    :return: bool
    """
    result = pm.del_data_in_warehouse(name, color, grade)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return {'status': 'ok'}


@router.patch('/clear-warehouse')
def clear_warehouse() -> dict:
    """
    Удаляет все записи со склада
    :return: None
    """
    pm.clear_warehouse()

    return {'status': 'ok'}


@router.patch('/clear-warehouse')
def clear_statistic() -> dict:
    """
    Удаляет все записи из отдела статистики
    :return: None
    """
    pm.clear_statistic()

    return {'status': 'ok'}