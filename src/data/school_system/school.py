from model.school_system.school import School

class Schools:
    __schools = []
    
    @classmethod
    def get_one(cls, name: str) -> School | None:
        for school in cls.__schools:
            pass

    @classmethod
    def get_all(cls) -> list[School]:
        pass

    @classmethod
    def create(cls, creature: School) -> bool:
        pass

    @classmethod
    def delete(cls, id: int) -> bool:
        pass