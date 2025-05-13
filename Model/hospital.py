from Model.doctor import Doctor

class Hospital:
    def __init__(self, hospital_name):
        self.__hospital_name = hospital_name
        self.__doctors = []

    @property
    def hospital_name(self):
        return self.__hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self.__hospital_name = value

    @property
    def doctors(self):
        return self.__doctors

    def add_doctor(self, doctor):
        if isinstance(doctor, Doctor):
            self.__doctors.append(doctor)

    def get_doctors(self):
        return self.__doctors
