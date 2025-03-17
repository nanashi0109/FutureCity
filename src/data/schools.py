from src.model.school import School

class Schools:
    __schools = []
    
    @classmethod
    async def get_one(cls, id: int) -> School | None:
        for school in cls.__schools:
            if school.id == id:
                return school

    @classmethod
    async def get_all(cls) -> list[School]:
        return cls.__schools

    @classmethod
    async def create(cls, school_to_add: School) -> bool:
        insert_id = 1
        for school in cls.__schools:
            if school.id == insert_id:
                insert_id += 1
            else:
                break

        school_to_add.id = insert_id

        cls.__schools.append(school_to_add)
        return True

    @classmethod
    async def delete(cls, id: int) -> bool:
        for school in cls.__schools:
            if school.id == id:
                cls.__schools.remove(school)
                return True
        return False

    @classmethod
    async def update(cls, school_to_update: School) -> bool:
        for school in cls.__schools:
            if school.id == school_to_update.id:
                school.name = school_to_update.name
                school.students = school_to_update.students
                school.teachers = school_to_update.teachers