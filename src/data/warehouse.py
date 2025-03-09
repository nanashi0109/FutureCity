from src.model.resource import Resource

class ProcessingMining:

    __warehouse = []

    __statistic = []

    @classmethod
    def add_resource(cls, data: Resource) -> None:
        """
        Добавляет Полученные ресурсы на склад на склад, суммирует количество добытых ресурсов если идентичные есть на складе,
        Также добавляет данные о ежедневной добыче ресурсов в отдел статистики
        :param data: принимает сведения о добытых ресурсах за указанную дату
        :return: None
        """
        cls.__statistic.append(data)

        del data['date']

        if len(cls.__warehouse) != 0:

            for elem in cls.__warehouse:
                if elem.name != data.name or elem.category != data.category or elem.color != data.color or elem.grade != data.grade:
                    cls.__warehouse.append(data)

                else:
                    elem.weight += data.weight
        else:
            cls.__warehouse.append(data)


    @classmethod
    def edit_weight_resource(cls, name: str, category : str, color: str, grade: str,  weight: float) -> bool:
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

            elem.weight += weight
            return True

