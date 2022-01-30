from flask_restful import Resource, Api, request
from package.model import conn



class Wards(Resource):
    """This contain apis to carry out activity with all wards"""

    def get(self):
        """Retrieve all the ward and return in form of json"""

        ward = conn.execute("SELECT * from Wards").fetchall()
        return ward

    def post(self):
        """Api to add ward in the database"""

        ward = request.get_json(force=True)
        Ward_ID = ward['Ward_ID']
        Ward_Name = ward['Ward_Name']
        conn.execute('''INSERT INTO Wards(Ward_ID, Ward_Name) VALUES(?,?)''', (Ward_ID, Ward_Name))
        conn.commit()
        return ward



class Ward(Resource):
    """This contain all api doing activity with single ward"""

    def get(self,Ward_ID):
        """retrieve a singe ward details by its Ward_ID"""

        ward = conn.execute("SELECT * FROM Wards WHERE Ward_ID=?",(Ward_ID,)).fetchall()
        return ward


    def delete(self,Ward_ID):
        """Delete the ward by its Ward_ID"""

        conn.execute("DELETE FROM Wards WHERE Ward_ID=?",(Ward_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Ward_ID):
        """Update the ward details by the Ward_ID"""

        ward = request.get_json(force=True)
        Ward_Name = ward['Ward_Name']
        conn.execute("UPDATE Wards SET Ward_Name=? WHERE Ward_ID=?", (Ward_Name, Ward_ID))
        conn.commit()
        return ward