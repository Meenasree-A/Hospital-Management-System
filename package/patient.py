from flask_restful import Resource, Api, request
from package.model import conn

class Patients(Resource):
    """It contain all the api carrying the activity with specific patient"""

    def get(self):
        """Api to retrieve all the Patient from the database"""

        patients = conn.execute("SELECT * FROM Patient").fetchall()
        return patients



    def post(self):
        """api to add the patient in the database"""

        patientInput = request.get_json(force=True)
        First_Name=patientInput['First_Name']
        Last_Name = patientInput['Last_Name']
        Address = patientInput['Address']
        Age = patientInput['Age']
        Gender = patientInput['Gender']
        Insurance_ID = patientInput['Insurance_ID']
        Mobile_Number = patientInput['Mobile_Number']
        Email_Address = patientInput['Email_Address']
        SSN = patientInput['SSN']
        patientInput['Patient_ID']=conn.execute('''INSERT INTO Patient(First_Name,Last_Name,Address,Age,Gender,Insurance_ID,Mobile_Number,Email_Address,SSN)
            VALUES(?,?,?,?,?,?,?,?,?)''', (First_Name,Last_Name,Address,Age,Gender,Insurance_ID,Mobile_Number,Email_Address,SSN)).lastrowid
        conn.commit()
        return patientInput

class Patient(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrieve details of the patient by it id"""

        patient = conn.execute("SELECT * FROM Patient WHERE Patient_ID=?",(id,)).fetchall()
        return patient

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM Patient WHERE Patient_ID=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patientInput = request.get_json(force=True)
        First_Name=patientInput['First_Name']
        Last_Name = patientInput['Last_Name']
        Address = patientInput['Address']
        Age = patientInput['Age']
        Gender = patientInput['Gender']
        Insurance_ID = patientInput['Insurance_ID']
        Mobile_Number = patientInput['Mobile_Number']
        Email_Address = patientInput['Email_Address']
        SSN = patientInput['SSN']
        Patient_ID = patientInput['Patient_ID']
        conn.execute("UPDATE Patient SET First_Name=?,Last_Name=?,Address=?,Age=?,Gender=?,Insurance_ID=?,Mobile_Number=?, Email_Address=?, SSN=? WHERE Patient_ID=?",
                     (First_Name,Last_Name,Address,Age,Gender,Insurance_ID,Mobile_Number,Email_Address,SSN,Patient_ID))
        conn.commit()
        return patientInput