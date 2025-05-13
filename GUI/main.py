import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMessageBox,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
)
from Controller.controller import Controller

class HospitalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sistema de Información Hospitalaria')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.hospital_name_input = QLineEdit()
        self.hospital_name_input.setPlaceholderText('Nombre del Hospital')
        create_hospital_btn = QPushButton('Crear Hospital')
        create_hospital_btn.clicked.connect(self.create_hospital)

        layout.addWidget(QLabel('Crear Hospital:'))
        layout.addWidget(self.hospital_name_input)
        layout.addWidget(create_hospital_btn)

        self.doctor_name_input = QLineEdit()
        self.doctor_name_input.setPlaceholderText('Nombre del Doctor')
        self.speciality_input = QLineEdit()
        self.speciality_input.setPlaceholderText('Especialidad')
        self.dni_input = QLineEdit()
        self.dni_input.setPlaceholderText('DNI')
        add_doctor_btn = QPushButton('Añadir Doctor')
        add_doctor_btn.clicked.connect(self.add_doctor)

        layout.addWidget(QLabel('Añadir Doctor:'))
        layout.addWidget(self.doctor_name_input)
        layout.addWidget(self.speciality_input)
        layout.addWidget(self.dni_input)
        layout.addWidget(add_doctor_btn)

        self.search_dni_input = QLineEdit()
        self.search_dni_input.setPlaceholderText('DNI para buscar')
        search_btn = QPushButton('Buscar Doctor')
        search_btn.clicked.connect(self.search_doctor)

        layout.addWidget(QLabel('Buscar Doctor por DNI:'))
        layout.addWidget(self.search_dni_input)
        layout.addWidget(search_btn)

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(4)
        self.result_table.setHorizontalHeaderLabels(['Hospital', 'Doctor', 'Especialidad', 'DNI'])

        layout.addWidget(self.result_table)

        self.setLayout(layout)
        self.hospital = None

    def create_hospital(self):
        name = self.hospital_name_input.text()
        if not name:
            QMessageBox.warning(self, "Error", "Por favor escriba el nombre del hospital.", QMessageBox.StandardButton.Ok)
            return
        
        # Verifica si el hospital ya existe
        for hospital in self.controller.hospitals:
            if hospital.hospital_name == name:
                QMessageBox.warning(self, "Error", "El hospital ya existe.", QMessageBox.StandardButton.Ok)
                return
        
        self.hospital = self.controller.create_hospital(name)
        self.hospital_name_input.clear()
        QMessageBox.information(self, "Éxito", "Hospital agregado con éxito.", QMessageBox.StandardButton.Ok)

    def add_doctor(self):
        if self.hospital:
            doctor_name = self.doctor_name_input.text()
            speciality = self.speciality_input.text()
            dni = self.dni_input.text()
            if not doctor_name or not speciality or not dni:
                QMessageBox.warning(self, "Error", "Por favor complete todos los campos del doctor.", QMessageBox.StandardButton.Ok)
                return

            # Verifica si el doctor ya existe en el hospital
            for doctor in self.hospital.get_doctors():
                if doctor.dni == dni:
                    QMessageBox.warning(self, "Error", "El doctor ya existe en este hospital.", QMessageBox.StandardButton.Ok)
                    return

            self.controller.add_doctor_to_hospital(self.hospital, doctor_name, speciality, dni)
            self.doctor_name_input.clear()
            self.speciality_input.clear()
            self.dni_input.clear()
            QMessageBox.information(self, "Éxito", "Doctor agregado con éxito.", QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self, "Error", "Por favor cree un hospital primero.", QMessageBox.StandardButton.Ok)
        
    def search_doctor(self):
        dni = self.search_dni_input.text()
        result = self.controller.search_by_dni(dni)
        self.result_table.setRowCount(0)

        if result:
            self.result_table.insertRow(0)
            self.result_table.setItem(0, 0, QTableWidgetItem(result['hospital_name']))
            self.result_table.setItem(0, 1, QTableWidgetItem(result['doctor_name']))
            self.result_table.setItem(0, 2, QTableWidgetItem(result['speciality']))
            self.result_table.setItem(0, 3, QTableWidgetItem(result['dni']))
        else:
            QMessageBox.warning(self, "Error", "No se encontró ningún doctor con ese DNI.", QMessageBox.StandardButton.Ok)
            self.result_table.setRowCount(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HospitalApp()
    window.show()
    sys.exit(app.exec_())