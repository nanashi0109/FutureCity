from fastapi import Body, APIRouter, HTTPException
from src.data.warehouse import ProcessingMining as pm

router = APIRouter(prefix='/mining')


@router.get('/all-statistic')
def get_all_statistic() -> list:
    """
    Возвращает всю статистику о выработке ресурсов, содержащуюся в базе
    :return: list
    """
    result = pm.get_all_statistic()

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
    result = pm.get_statistic_for_date(date)

    if not result:
        raise HTTPException(status_code=404, detail='Данные по запросу отсутствуют')

    return result