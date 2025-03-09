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



