from model.school_system.student import Student

class Students:
    __students = []
    
    @classmethod
    def get_one(cls, name: str) -> Student | None:
        for student in cls.__students:
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