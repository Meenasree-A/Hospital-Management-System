#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn



class Medications(Resource):
    """This contain apis to carry out activity with all medicines"""

    def get(self):
        """Retrieve all the medicine details and return in form of json"""

        medication = conn.execute("SELECT * from Medicine").fetchall()
        return medication

    def post(self):
        """Api to add medicine in the database"""

        medication = request.get_json(force=True)
        Medicine_ID = medication['Medicine_ID']
        Medicine_Name = medication['Medicine_Name']
        Cost = medication['Cost']
        conn.execute('''INSERT INTO Medicine(Medicine_ID, Medicine_Name, Cost) VALUES(?,?,?)''', (Medicine_ID, Medicine_Name, Cost))
        conn.commit()
        return medication



class Medication(Resource):
    """This contain all api doing activity with single medicine"""

    def get(self,Medicine_ID):
        """retrive a singe medicine details by its Medicine_ID"""

        medication = conn.execute("SELECT * FROM Medicine WHERE Medicine_ID=?",(Medicine_ID,)).fetchall()
        return medication


    def delete(self,Medicine_ID):
        """Delete the medicine by its ID"""

        conn.execute("DELETE FROM Medicine WHERE Medicine_ID=?",(Medicine_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Medicine_ID):
        """Update the medicine details by the Medicine_ID"""

        medication = request.get_json(force=True)
        Medicine_Name = medication['Medicine_Name']
        Cost = medication['Cost']
        conn.execute("UPDATE Medicine SET Medicine_Name=?, Cost=? WHERE Medicine_ID=?", (Medicine_Name, Cost,Medicine_ID))
        conn.commit()
        return medication