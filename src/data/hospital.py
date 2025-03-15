from src.model.hospital import Hospital

class Hospitals:
    __hospitals = []

    @classmethod
    def get_one(cls, id: int):
        for hospital in cls.__hospitals:
            if hospital.id == id:
                return hospital


    @classmethod
    def get_all(cls):
        return cls.__hospitals

    @classmethod
    def create(cls,new_hospital:Hospital):
        for hospital in cls.__hospitals:
            if hospital.id == new_hospital.id:
                new_hospital.id = len(cls.__hospitals) + 1
                break
        cls.__hospitals.append(new_hospital)



    @classmethod
    def delete(cls, id: int):
        for hospital in cls.__hospitals:
            if hospital.id == id:
                cls.__hospitals.remove(hospital)
                return True
            return False


    @classmethod
    def update(cls, new_hospital: Hospital):
        for hospital in cls.__hospitals:
            if hospital.id == new_hospital.id:
                hospital.name = new_hospital.name
                hospital.id = new_hospital.id
                hospital.patients = new_hospital.patients


