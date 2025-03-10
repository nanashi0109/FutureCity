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
        if len(cls.__statistic) == 0:
            return False

        return [elem for elem in cls.__statistic if elem.date == date]




    @classmethod
    def get_statistic_for_category(cls, category: str) -> float | bool:
        """
        Возвращает общее количество ресурса полученной категории хранится на складе, с любыми характеристиками
        :param category: принимает название категории (ore, stone, wood....)
        :return: float
        """
        if len(cls.__statistic) == 0:
            return False

        return sum(elem.weight for elem in cls.__statistic if elem.category == category)



    @classmethod
    def get_statistic_resource(cls, resource: Resource) -> float | bool:
        """
        Возвращает количество ресурса по строго заданным характеристикам хранящегося на складе
        :param resource: принимает объект ресурса со всеми его характеристиками
        :return: float | bool
        """
        if len(cls.__statistic) == 0:
            return False

        return sum(elem.weight for elem in cls.__statistic if elem.name == resource.name and elem.category == resource.category and elem.color == resource.color and elem.grade == resource.grade)


    @classmethod
    def get_statistic_for_citizen(cls, name: str) -> list | bool:
        """
        Возвращает всю выработку горожанина за весь период, согласно полученному имени
        :param name: принимает имя горожанина
        :return: list
        """
        if len(cls.__statistic) == 0:
            return False

        return [elem for elem in cls.__statistic if name == elem.citizen.name]


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
        del resource['citizen']

        if len(cls.__warehouse) != 0:

            for elem in cls.__warehouse:
                if elem.name == resource.name and elem.category == resource.category and elem.color == resource.color and elem.grade == resource.grade:
                    elem.weight += resource.weight

            cls.__warehouse.append(resource)

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
            if elem.name == name and elem.category == category and color == color and elem.grade == grade:
                elem.weight = weight
                return True

        return False


