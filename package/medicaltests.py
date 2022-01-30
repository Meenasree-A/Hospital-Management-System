from flask_restful import Resource, Api, request
from package.model import conn



class Medicaltests(Resource):
    """This contain apis to carry out activity with all Medical tests"""

    def get(self):
        """Retrieve all the Medical tests and return in form of json"""

        medicaltests = conn.execute("SELECT * from Medical_Tests").fetchall()
        return medicaltests

    def post(self):
        """Api to add Medical tests in the database"""

        medicaltests = request.get_json(force=True)
        Test_ID = medicaltests['Test_ID']
        Test_Name = medicaltests['Test_Name']
        Test_Cost = medicaltests['Test_Cost']
        Patient_Patient_ID = medicaltests['Patient_Patient_ID']
        conn.execute('''INSERT INTO Medical_Tests(Test_ID, Test_Name, Test_Cost, Patient_Patient_ID) VALUES(?,?,?,?)''', (Test_ID, Test_Name, Test_Cost, Patient_Patient_ID))
        conn.commit()
        return medicaltests



class Medicaltest(Resource):
    """This contain all api doing activity with single Medical test"""

    def get(self,Test_ID):
        """retrieve a singe Medical test details by its code"""

        medicaltests = conn.execute("SELECT * FROM Medical_Tests WHERE Test_ID=?",(Test_ID,)).fetchall()
        return medicaltests


    def delete(self,Test_ID):
        """Delete the Medical test by its ID"""

        conn.execute("DELETE FROM Medical_Tests WHERE Test_ID=?",(Test_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Test_ID):
        """Update the Medical test details by the ID"""

        medicaltests = request.get_json(force=True)
        Test_Name = medicaltests['Test_Name']
        Test_Cost = medicaltests['Test_Cost']
        conn.execute("UPDATE Medical_Tests SET Test_Name=?,Test_Cost=? WHERE Test_ID=?", (Test_Name, Test_Cost, Test_ID))
        conn.commit()
        return medicaltests