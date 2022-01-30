from flask import Flask,send_from_directory,render_template
from flask import send_from_directory
from flask_restful import Resource, Api
from package.patient import Patients, Patient
from package.doctor import Doctors, Doctor
from package.appointment import Appointments, Appointment
from package.common import Common
from package.medication import Medication, Medications
from package.department import Departments, Department
from package.receptionist import Receptionists, Receptionist
from package.nurse import Nurse, Nurses
from package.room import Room, Rooms
from package.procedure import Procedure, Procedures 
from package.ward import Ward, Wards
from package.patienthistory import Patienthistories, Patienthistory
from package.medicaltests import Medicaltests, Medicaltest
from package.reports import Reports, Report
from package.bill import bills

import json
import os

with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Appointments, '/appointment')
api.add_resource(Appointment, '/appointment/<int:Appointment_ID>')
api.add_resource(Common, '/common')
api.add_resource(Medications, '/medication')
api.add_resource(Medication, '/medication/<int:Medicine_ID>')
api.add_resource(Receptionists, '/receptionist')
api.add_resource(Receptionist, '/receptionist/<int:Rep_ID>')
api.add_resource(Departments, '/department')
api.add_resource(Department, '/department/<int:Department_ID>')
api.add_resource(Nurses, '/nurse')
api.add_resource(Nurse, '/nurse/<int:Nurse_ID>')
api.add_resource(Rooms, '/room')
api.add_resource(Room, '/room/<int:Room_ID>')
api.add_resource(Wards, '/ward')
api.add_resource(Ward, '/ward/<int:Ward_ID>')
api.add_resource(Patienthistories, '/patienthistory')
api.add_resource(Patienthistory, '/patienthistory/<int:Patient_Patient_ID>')
api.add_resource(Medicaltests, '/medicaltests')
api.add_resource(Medicaltest, '/medicaltests/<int:Test_ID>')
api.add_resource(Reports, '/reports')
api.add_resource(Report, '/reports/<int:Report_ID>')
api.add_resource(bills, '/bill')
api.add_resource(Procedures, '/procedure')
api.add_resource(Procedure, '/procedure/<int:Operation_ID>')


# Routes

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])