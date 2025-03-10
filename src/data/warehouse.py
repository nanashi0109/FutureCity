from src.model import resource
from src.model.resource import Resource

class ProcessingMining:

    __warehouse = []

    __statistic = []


    @classmethod
    def get_all_statistic(cls) -> list:
        """
        Возвращает всю статистику о выработке ресурсов, содержащуюся в базе
        :return: list
        """
        return cls.__statistic


    @classmethod
    def get_statistic_for_date(cls, date: str) -> list | bool:
        """
        Возвращает статистику о выработке ресурсов за полученную дату, если такая имеется
        :param date: принимает дату, по которой осуществляется поиск данных о выработке ресурсов
        :return: list | bool
        """
        result_lst = []

        if len(cls.__statistic) == 0:
            return False

        for elem in cls.__statistic:
            if elem.date == date:
                result_lst.append(elem)

        return result_lst


    @classmethod
    def get_statistic_for_category(cls, category: str) -> float | bool:
        """
        Возвращает общее количество ресурса полученной категории хранится на складе, с любыми характеристиками
        :param category: принимает название категории (ore, stone, wood....)
        :return: float
        """
        result = 0

        if len(cls.__statistic) == 0:
            return False

        for elem in cls.__statistic:
            if elem.category == category:
                result += elem.weight

        return result


    @classmethod
    def get_statistic_resource(cls, resource: Resource) -> float | bool:
        """
        Возвращает количество ресурса по строго заданным характеристикам хранящийся на складе
        :param resource: принимает объект ресурса со всеми его характеристиками
        :return: float | bool
        """
        result = 0

        if len(cls.__statistic) == 0:
            return False

        for elem in cls.__statistic:
            if elem.name == resource.name and elem.category == resource.category and elem.color == resource.color and elem.grade == resource.grade:
                result += elem.weight

        return result


    @classmethod
    def add_resource(cls, resource: Resource) -> None:
        """
        Добавляет Полученные ресурсы на склад на склад, суммирует количество добытых ресурсов если идентичные есть на складе,
        Также добавляет данные о ежедневной добыче ресурсов в отдел статистики
        :param resource: принимает сведения о добытых ресурсах за указанную дату
        :return: None
        """
        cls.__statistic.append(resource)

        del resource['date']

        if len(cls.__warehouse) != 0:

            for elem in cls.__warehouse:
                if elem.name != resource.name or elem.category != resource.category or elem.color != resource.color or elem.grade != resource.grade:
                    cls.__warehouse.append(resource)

                else:
                    elem.weight += resource.weight
        else:
            cls.__warehouse.append(resource)


    @classmethod
    def update_weight_resource(cls, name: str, category : str, color: str, grade: str,  weight: float) -> bool:
        """
        Изменяет количество ресурса на складе если идентичные есть на складе, например если часть ресурса уже израсходована
        :param name: принимает название ресурса,
        :param category: принимает категорию ресурса (дерево, железо, уголь ....)
        :param color: принимает цвет ресурса,
        :param grade: принимает марку ресурса (A/B/C)
        :param weight: принимает новое количество указанного ресурса на складе
        :return: bool
        """
        if len(cls.__warehouse) == 0:
            return False

        for elem in cls.__warehouse:
            if elem.name != name or elem.category != category or color != color or elem.grade != grade:
                return False

            elem.weight = weight
            return True


