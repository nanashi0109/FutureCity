from model.school_system.teacher import Teacher

class Teachers:
    __teachers = []
    
    @classmethod
    def get_one(cls, id: int) -> Teacher | None:
        for teacher in cls.__teachers:
            if teacher.id == id:
                return teacher

    @classmethod
    def get_all(cls) -> list[Teacher]:
        return cls.__teachers

    @classmethod
    def create(cls, teacher_to_add: Teacher) -> bool:
        insert_id = 1
        for teacher in cls.__teachers:
            if teacher.id == insert_id:
                insert_id += 1
            else:
                break

        teacher_to_add.id = insert_id

        cls.__teachers.append(teacher_to_add)
        return True

    @classmethod
    def delete(cls, id: int) -> bool:
        for teacher in cls.__teachers:
            if teacher.id == id:
                cls.__teachers.remove(teacher)
                return True
        return False

    @classmethod
    def update(cls, teacher_to_update: Teacher) -> bool:
        for teacher in cls.__teachers:
            if teacher.id == teacher_to_update.id:
                teacher.name = teacher_to_update.name
                teacher.school_id = teacher_to_update.school_id