from src.model.citizens import Citizen

class CitizenData:
    __citizens = []

    @classmethod
    async def get_one(cls, id: int) -> Citizen:
        for citizen in cls.__citizens:
            if citizen.id == id:
                return citizen

    @classmethod
    async def get_all(cls) -> list[Citizen]:
        return cls.__citizens

    @classmethod
    async def add(cls, citizen: Citizen) -> bool:
        ids = [citizen.id for citizen in cls.__citizens]
        
        if citizen.id not in ids:
            if citizen.id is None:
                citizen.id = cls.get_last_id()
                
            cls.__citizens.append(citizen)
            return True
        
        return False

    @classmethod
    async def remove(cls, id: int) -> Citizen:
        target_citizen = cls.get_one(id)

        cls.__citizens.remove(target_citizen)

    @classmethod
    async def update(cls, citizen: Citizen) -> None:
        target_citizen = cls.get_one(citizen)
        cls.remove(target_citizen)
        cls.add(citizen)

    @classmethod
    def get_last_id(cls) -> int:   
        if len(cls.__citizens) == 0:
            return 0
        
        return max([citizen.id for citizen in cls.__citizens]) + 1