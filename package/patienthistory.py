from flask_restful import Resource, Api, request
from package.model import conn



class Patienthistories(Resource):
    """This contain apis to carry out activity with all patient histories"""

    def get(self):
        """Retrive the histories and return in form of json"""

        patienthistory = conn.execute("SELECT * from Patient_History").fetchall()
        return patienthistory

    def post(self):

        patienthistory = request.get_json(force=True)
        Issue_Description = patienthistory['Issue_Description']
        Visited_Date = patienthistory['Visited_Date']
        Patient_Patient_ID = patienthistory['Patient_Patient_ID']
        patienthistory['app_id'] = conn.execute('''INSERT INTO Patient_History(Issue_Description,Visited_Date,Patient_Patient_ID)
            VALUES(?,?,?)''', (Issue_Description,Visited_Date,Patient_Patient_ID)).lastrowid
        conn.commit()
        return patienthistory



class Patienthistory(Resource):
    """This contain all api doing activity with single Patient"""

    def get(self,Patient_Patient_ID):
        """retrieve a singe Patient details by patient's id"""

        patienthistory = conn.execute("SELECT * FROM Patient_History WHERE Patient_Patient_ID=?",(Patient_Patient_ID,)).fetchall()
        return patienthistory


    def delete(self,Patient_Patient_ID):
        """Delete the history by patient's id"""

        conn.execute("DELETE FROM Patient_History WHERE Patient_Patient_ID=?",(Patient_Patient_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Patient_Patient_ID):
        """Update the history by the patient id"""

        patienthistory = request.get_json(force=True)
        Issue_Description = patienthistory['Issue_Description']
        Visited_Date = patienthistory['Visited_Date']
        conn.execute("UPDATE Patient_History SET Issue_Description=?,Visited_Date=? WHERE Patient_Patient_ID=?",
                     (Issue_Description, Visited_Date, Patient_Patient_ID))
        conn.commit()
        return patienthistory