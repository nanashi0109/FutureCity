from model.school_system.teacher import Teacher

class Teachers:
    __teachers = []
    
    @classmethod
    def get_one(cls, name: str) -> Teacher | None:
        for teacher in cls.__teachers:
            pass

    @classmethod
    def get_all(cls) -> list[Teacher]:
        pass

    @classmethod
    def create(cls, creature: Teacherr) -> bool:
        pass

    @classmethod
    def delete(cls, id: int) -> bool:
        pass