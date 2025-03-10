from fastapi import Body, APIRouter, HTTPException
from src.data.warehouse import ProcessingMining as pm

router = APIRouter(prefix='/mining')


@router.get('/all-statistic')
def get_all_statistic() -> list:
    """
    Возвращает всю статистику о выработке ресурсов, содержащуюся в базе
    :return: list
    """
    result = pm.return_all_statistic()

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return result


@router.get('/statistic-for-date')
def get_statistic_for_date(date: str) -> list:
    """
    Возвращает статистику о выработке ресурсов за полученную дату, если такая имеется
    :param date: принимает дату, по которой осуществляется поиск данных о выработке ресурсов
    :return: list
    """
    result = pm.return_statistic_for_date(date)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return result


@router.get('/weight-for-category')
def get_weight_for_category(category: str) -> float:
    """
    Возвращает общее количество ресурса полученной категории которое хранится на складе, с любыми характеристиками, если он имеется
    :param category: принимает название категории (ore, stone, wood....)
    :return: float | bool
    """
    result = pm.return_weight_for_category(category)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return result


@router.get('/weight-for-params')
def get_weight_for_params(name: str, color: str, grade: str) -> float:
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

    return result