from flask_restful import Resource, Api, request
from package.model import conn
class Nurses(Resource):
    """This contain apis to carry out activity with all nurses"""

    def get(self):
        """Retrieve list of all the nurses"""

        nurses = conn.execute("SELECT * FROM Nurse").fetchall()
        return nurses



    def post(self):
        """Add new nurse"""

        nurseInput = request.get_json(force=True)
        First_Name=nurseInput['First_Name']
        Last_Name = nurseInput['Last_Name']
        Mobile_Number = nurseInput['Mobile_Number']
        SSN = nurseInput['SSN']
        Wards_Ward_ID = nurseInput['Wards_Ward_ID']
        nurseInput['Nurse_ID']=conn.execute('''INSERT INTO nurse(First_Name,Last_Name,Mobile_Number,SSN,Wards_Ward_ID)
            VALUES(?,?,?,?,?)''', (First_Name, Last_Name,Mobile_Number,SSN,Wards_Ward_ID)).lastrowid
        conn.commit()
        return nurseInput

class Nurse(Resource):
    """It includes all the apis carrying out the activity with the single nurse"""


    def get(self,Nurse_ID):
        """get the details of the nurse by the nurse id"""

        nurse = conn.execute("SELECT * FROM nurse WHERE Nurse_ID=?",(id,)).fetchall()
        return nurse

    def delete(self, Nurse_ID):
        """Delete the nurse by its id"""

        conn.execute("DELETE FROM nurse WHERE Nurse_ID=?", (Nurse_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Nurse_ID):
        """Update the nurse by its id"""

        nurseInput = request.get_json(force=True)
        First_Name=nurseInput['First_Name']
        Last_Name = nurseInput['Last_Name']
        Mobile_Number = nurseInput['Mobile_Number']
        SSN = nurseInput['SSN']
        Wards_Ward_ID = nurseInput['Wards_Ward_ID']
        conn.execute(
            "UPDATE nurse SET First_Name=?,Last_Name=?,Mobile_Number=?,SSN=?,Wards_Ward_ID=? WHERE Nurse_ID=?",
            (First_Name, Last_Name, Mobile_Number, SSN, Wards_Ward_ID, Nurse_ID))
        conn.commit()
        return nurseInput