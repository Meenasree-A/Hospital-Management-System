from flask_restful import Resource, Api, request
from package.model import conn



class Reports(Resource):
    """This contain apis to carry out activity with all reports"""

    def get(self):
        """Retrieve all the reports and return in form of json"""

        reports = conn.execute("SELECT * from Reports").fetchall()
        return reports

    def post(self):
        """Api to add reports in the database"""

        reports = request.get_json(force=True)
        Report_ID = reports['Report_ID']
        Name = reports['Name']
        Description = reports['Description']
        Medical_Tests_Test_ID = reports['Medical_Tests_Test_ID']
        Patient_Patient_ID = reports['Patient_Patient_ID']
        conn.execute('''INSERT INTO Reports(Report_ID,Name, Description, Medical_Tests_Test_ID, Patient_Patient_ID) VALUES(?,?,?,?,?)''', (Report_ID, Name, Description, Medical_Tests_Test_ID, Patient_Patient_ID))
        conn.commit()
        return reports



class Report(Resource):
    """This contain all api doing activity with single report"""

    def get(self,Report_ID):
        """retrive a singe report details by its code"""

        reports = conn.execute("SELECT * FROM Reports WHERE Report_ID=?",(Report_ID,)).fetchall()
        return reports


    def delete(self,Report_ID):
        """Delete the report by its ID"""

        conn.execute("DELETE FROM Reports WHERE Report_ID=?",(Report_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Report_ID):
        """Update the report details by the ID"""

        reports = request.get_json(force=True)
        Name = reports['Name']
        Description = reports['Description']
        Medical_Tests_Test_ID = reports['Medical_Tests_Test_ID']
        Patient_Patient_ID = reports['Patient_Patient_ID']
        conn.execute("UPDATE Reports SET Name=?, Description=?, Medical_Tests_Test_ID=?, Patient_Patient_ID=? WHERE Report_ID=?", (Name, Description, Medical_Tests_Test_ID, Patient_Patient_ID, Report_ID))
        conn.commit()
        return reports