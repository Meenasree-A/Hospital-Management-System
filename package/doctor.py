from flask_restful import Resource, Api, request
from package.model import conn
class Doctors(Resource):

    def get(self):
        """Retrieve list of all the doctors"""

        doctors = conn.execute("SELECT * FROM Doctor").fetchall()
        return doctors



    def post(self):
        """Add new doctor information"""

        doctorInput = request.get_json(force=True)
        First_Name=doctorInput['First_Name']
        Last_Name = doctorInput['Last_Name']
        Mobile_Number = doctorInput['Mobile_Number']
        SSN = doctorInput['SSN']
        Specialisation = doctorInput['Specialisation']
        Department_Department_ID = doctorInput['Department_Department_ID']
        doctorInput['Doctor_ID']=conn.execute('''INSERT INTO doctor(First_Name,Last_Name,Mobile_Number,SSN,Specialisation,Department_Department_ID)
            VALUES(?,?,?,?,?,?)''', (First_Name, Last_Name,Mobile_Number,SSN,Specialisation,Department_Department_ID)).lastrowid
        conn.commit()
        return doctorInput

class Doctor(Resource):
    """It includes all the apis carrying out the activities with the single doctor"""


    def get(self,id):
        """get the details of the docktor by the doctor id"""

        doctor = conn.execute("SELECT * FROM Doctor WHERE Doctor_ID=?",(id,)).fetchall()
        return doctor

    def delete(self, id):
        """Delete the doctor by its id"""

        conn.execute("DELETE FROM Doctor WHERE Doctor_ID=?", (id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """Update the doctor by its id"""

        doctorInput = request.get_json(force=True)
        First_Name=doctorInput['First_Name']
        Last_Name = doctorInput['Last_Name']
        Mobile_Number = doctorInput['Mobile_Number']
        SSN = doctorInput['SSN']
        Specialisation = doctorInput['Specialisation']
        Department_Department_ID = doctorInput['Department_Department_ID']
        Doctor_ID = doctorInput['Doctor_ID']
        conn.execute(
            "UPDATE doctor SET First_Name=?,Last_Name=?,Mobile_Number=?,SSN=?,Specialisation=?,Department_Department_ID=? WHERE Doctor_ID=?",
            (First_Name, Last_Name, Mobile_Number, SSN, Specialisation,Department_Department_ID, Doctor_ID))
        conn.commit()
        return doctorInput