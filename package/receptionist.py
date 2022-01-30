#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn



class Receptionists(Resource):
    """This contain apis to carry out activity with all appiontments"""

    def get(self):
        """Retrieve all the Receptionist and return in form of json"""

        # Receptionist = conn.execute("SELECT * from Receptionist").fetchall()
        Receptionist = conn.execute("SELECT * FROM Receptionist").fetchall()
        return Receptionist

    def post(self):
        """Api to add Receptionist in the database"""

        Receptionist = request.get_json(force=True)
        Rep_ID = Receptionist['Rep_ID']
        Name = Receptionist['Name']
        SSN = Receptionist['SSN']
        Mobile_Number = Receptionist['Mobile_Number']
        conn.execute('''INSERT INTO Receptionist(Rep_ID, Name, SSN, Mobile_Number) VALUES(?,?,?,?)''', (Rep_ID, Name, SSN, Mobile_Number))
        conn.commit()
        return Receptionist



class Receptionist(Resource):
    """This contain all api doing activity with single Receptionist"""

    def get(self,Rep_ID):
        """retrieve a singe department details by its id"""

        Receptionist = conn.execute("SELECT * FROM Receptionist WHERE Rep_ID=?",(Rep_ID,)).fetchall()
        return Receptionist


    def put(self,Rep_ID):
        """Update the Receptionist details by the receptionist id"""

        Receptionist = request.get_json(force=True)
        Name = Receptionist['Name']
        SSN = Receptionist['SSN']
        Mobile_Number = Receptionist['Mobile_Number']
        conn.execute("UPDATE Receptionist SET Name=?, SSN=?, Mobile_Number=?  WHERE Rep_ID=?", (Name, SSN, Mobile_Number,Rep_ID ))
        conn.commit()
        return Receptionist