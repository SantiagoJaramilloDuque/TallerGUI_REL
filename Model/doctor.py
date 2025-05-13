class Doctor:
    def __init__(self, doctor_name, speciality, dni):
        self.__doctor_name = doctor_name
        self.__speciality = speciality
        self.__dni = dni

    @property
    def doctor_name(self):
        return self.__doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self.__doctor_name = value

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, value):
        self.__speciality = value

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value
