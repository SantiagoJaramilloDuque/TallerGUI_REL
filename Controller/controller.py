from Model.hospital import Hospital
from Model.doctor import Doctor

class Controller:
    def __init__(self):
        self.hospitals = []

    def create_hospital(self, hospital_name):
        hospital = Hospital(hospital_name)
        self.hospitals.append(hospital)
        return hospital

    def add_doctor_to_hospital(self, hospital, doctor_name, speciality, dni):
        doctor = Doctor(doctor_name, speciality, dni)
        hospital.add_doctor(doctor)

    def search_by_dni(self, dni):
        for hospital in self.hospitals:
            for doctor in hospital.get_doctors():
                if doctor.dni == dni:
                    return {
                        'hospital_name': hospital.hospital_name,
                        'doctor_name': doctor.doctor_name,
                        'speciality': doctor.speciality,
                        'dni': doctor.dni
                    }
        return None
