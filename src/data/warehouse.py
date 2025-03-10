
from src.model.resource import Resource

class ProcessingMining:

    __warehouse = []

    __statistic = []


    @classmethod
    def return_all_statistic(cls) -> list:
        """
        Возвращает всю статистику о выработке ресурсов, содержащуюся в базе
        :return: list
        """
        return cls.__statistic


    @classmethod
    def return_statistic_for_date(cls, date: str) -> list | bool:
        """
        Возвращает статистику о выработке ресурсов за полученную дату, если такая имеется
        :param date: принимает дату, по которой осуществляется поиск данных о выработке ресурсов
        :return: list | bool
        """
        if len(cls.__statistic) == 0:
            return False

        return [elem for elem in cls.__statistic if elem.date == date]




    @classmethod
    def return_weight_for_category(cls, category: str) -> float | bool:
        """
        Возвращает общее количество ресурса полученной категории которое хранится на складе, с любыми характеристиками, если он имеется
        :param category: принимает название категории (ore, stone, wood....)
        :return: float | bool
        """
        if len(cls.__warehouse) == 0:
            return False

        return sum(elem.weight for elem in cls.__warehouse if elem.category == category)



    @classmethod
    def return_weight_for_params(cls, name: str, color: str, grade: str) -> float | bool:
        """
        Возвращает количество ресурса по строго заданным характеристикам хранящегося на складе, если он имеется
        :param name: название ресурса
        :param color: цвет ресурса
        :param grade: марка ресурса
        :return: float | bool
        """
        if len(cls.__warehouse) == 0:
            return False

        return sum(elem.weight for elem in cls.__warehouse if elem.name == name and elem.color == color and elem.grade == grade)


    @classmethod
    def return_statistic_for_citizen(cls, name: str) -> list | bool:
        """
        Возвращает всю выработку горожанина за весь период, согласно полученному имени
        :param name: принимает имя горожанина
        :return: list
        """
        if len(cls.__statistic) == 0:
            return False

        return [elem for elem in cls.__statistic if name == elem.citizen.name]


    @classmethod
    def add_resource_in_warehouse(cls, resource: Resource) -> None:
        """
        Добавляет Полученные ресурсы на склад и в отдел статистики, суммирует количество добытых ресурсов если идентичные есть на складе,
        Также добавляет данные о ежедневной добыче ресурсов в отдел статистики
        :param resource: принимает сведения о добытых ресурсах за указанную дату
        :return: None
        """
        cls.__statistic.append(resource)

        del resource['date']
        del resource['citizen']

        if len(cls.__warehouse) != 0:

            for elem in cls.__warehouse:
                if elem.name == resource.name and elem.color == resource.color and elem.grade == resource.grade:
                    elem.weight += resource.weight

            cls.__warehouse.append(resource)

        else:
            cls.__warehouse.append(resource)


    @classmethod
    def update_weight_resource_in_warehouse(cls, name: str, color: str, grade: str, weight: float) -> bool:
        """
        Изменяет количество ресурса на складе если идентичные есть на складе, например если часть ресурса уже израсходована
        :param name: название ресурса
        :param color: цвет ресурса
        :param grade: марка ресурса
        :param weight:марка ресурса
        :return: bool
        """
        if len(cls.__warehouse) == 0:
            return False

        for elem in cls.__warehouse:
            if elem.name == name and elem.color == color and elem.grade == grade:
                elem.weight = weight
                return True

        return False


    @classmethod
    def update_citizen_in_statistic(cls, resource: Resource) -> bool:
        """
        Изменяет горожанина, задействованного на добыче определенного ресурса
        :param resource: принимает сведения о добытых ресурсах за указанную дату
        :return: bool
        """
        if len(cls.__statistic) == 0:
            return False

        for elem in cls.__statistic:
            if elem.name == resource.name and elem.color == resource.color and elem.grade == resource.grade and elem.date == resource.date:
                elem.citizen = resource.citizen
                return True

        return False


    @classmethod
    def del_data_statistic(cls, resource: Resource) -> bool:
        """
        Удаляет из отдела статистики записи о добыче ресурсов, идентичные полученным
        :param resource: принимает сведения о добытых ресурсах за указанную дату
        :return: bool
        """
        if len(cls.__statistic) == 0:
            return False

        for elem in cls.__statistic:
            if elem.name == resource.name and elem.color == resource.color and elem.grade == resource.grade and elem.date == resource.date and elem.citizen == resource.citizen:
                del elem
                return True

        return False


    @classmethod
    def del_data_warehouse(cls, name: str, color: str, grade: str) -> bool:
        """
         Удаляет запись о наличии определенного ресурса со склада
        :param name: название ресурса
        :param color: цвет ресурса
        :param grade: марка ресурса
        :return: bool
        """
        if len(cls.__warehouse) == 0:
            return False

        for elem in cls.__warehouse:
            if elem.name == name and elem.color == color and elem.grade == grade:
                del elem
                return True

        return False


    @classmethod
    def clear_warehouse(cls):
        """
        Удаляет все записи со склада
        :return:
        """
        cls.__warehouse = []


    @classmethod
    def clear_statistic(cls):
        """
        Удаляет все записи из отдела статистики
        :return:
        """
        cls.__statistic = []


