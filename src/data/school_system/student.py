from model.school_system.student import Student

class Students:
    __students = []
    
    @classmethod
    def get_one(cls, id: int) -> Student | None:
        for student in cls.__students:
            if student.id == id:
                return student

    @classmethod
    def get_all(cls) -> list[Student]:
        return cls.__students

    @classmethod
    def create(cls, student_to_add: Student) -> bool:
        insert_id = 1
        for student in cls.__students:
            if student.id == insert_id:
                insert_id += 1
            else:
                break

        student_to_add.id = insert_id

        cls.__students.append(student_to_add)
        return True

    @classmethod
    def delete(cls, id: int) -> bool:
        for student in cls.__students:
            if student.id == id:
                cls.__students.remove(student)
                return True
        return False

    @classmethod
    def update(cls, student_to_update: Student) -> bool:
        for student in cls.__students:
            if student.id == student_to_update.id:
                student.name = student_to_update.name
                student.school_id = student_to_update.school_id