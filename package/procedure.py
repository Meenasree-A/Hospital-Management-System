from flask_restful import Resource, Api, request
from package.model import conn



class Procedures(Resource):
    """This contain apis to carry out activity with all Operations"""

    def get(self):
        """Retrive all the Operations and return in form of json"""

        procedure = conn.execute("SELECT * from Operations").fetchall()
        return procedure

    def post(self):
        """Api to add Operations in the database"""

        procedure = request.get_json(force=True)
        Operation_ID = procedure['Operation_ID']
        Operation_Name = procedure['Operation_Name']
        Cost = procedure['Cost']
        Patient_Patient_ID = procedure['Patient_Patient_ID']
        conn.execute('''INSERT INTO Operations(Operation_ID, Operation_Name, Cost, Patient_Patient_ID) VALUES(?,?,?,?)''', (Operation_ID, Operation_Name, Cost, Patient_Patient_ID))
        conn.commit()
        return procedure



class Procedure(Resource):
    """This contain all api doing activity with single operation"""

    def get(self,Operation_ID):
        """retrive a singe Operations details by its code"""

        procedure = conn.execute("SELECT * FROM Operations WHERE Operation_ID=?",(Operation_ID,)).fetchall()
        return procedure


    def delete(self,Operation_ID):
        """Delete the procedure by its code"""

        conn.execute("DELETE FROM Operations WHERE Operation_ID=?",(Operation_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Operation_ID):
        """Update the Operations details by the code"""

        procedure = request.get_json(force=True)
        Operation_Name = procedure['Operation_Name']
        Cost = procedure['Cost']
        conn.execute("UPDATE Operations SET Operation_Name=?,Cost=? WHERE Operation_ID=?", (Operation_Name, Cost, Operation_ID))
        conn.commit()
        return procedure