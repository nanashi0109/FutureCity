from src.model.Citizen import Citizen

class CitizenData:
    __citizens = []

    @classmethod
    def get_one(cls, id: int) -> Citizen:
        for citizen in cls.__citizens:
            if citizen.id == id:
                return citizen

    @classmethod
    def get_all(cls) -> list[Citizen]:
        return cls.__citizens

    @classmethod
    def add(cls, citizen: Citizen) -> bool:
        ids = [citizen.id for citizen in cls.__citizens]
        
        if citizen.id not in ids:
            cls.__citizens.append(citizen)
            return True
        
        return False

    @classmethod
    def remove(cls, id: int) -> Citizen:
        target_citizen = cls.get_one(id)

        cls.__citizens.remove(target_citizen)

    @classmethod
    def update(cls, citizen: Citizen) -> None:
        target_citizen = cls.get_one(citizen)
        cls.remove(target_citizen)
        cls.add(citizen)
