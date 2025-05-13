from Model.doctor import Doctor

class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.doctors = []

    def add_doctor(self, doctor):
        if isinstance(doctor, Doctor):
            self.doctors.append(doctor)

    def get_doctors(self):
        return self.doctors
