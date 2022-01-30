from flask_restful import Resource, Api, request
from package.model import conn



class Rooms(Resource):
    """This contain apis to carry out activity with all rooms"""

    def get(self):
        """Retrieve all the room and return in form of json"""

        room = conn.execute("SELECT * from Rooms").fetchall()
        return room

    def post(self):
        """Api to add rooms in the database"""

        room = request.get_json(force=True)
        Room_ID = room['Room_ID']
        Room_Name = room['Room_Name']
        Availability = room['Availability']
        Cost_of_Room = room['Cost_of_Room']
        Wards_Ward_ID = room['Wards_Ward_ID']
        conn.execute('''INSERT INTO Rooms(Room_ID, Room_Name, Availability, Cost_of_Room, Wards_Ward_ID) VALUES(?,?,?,?,?)''', (Room_ID, Room_Name, Availability, Cost_of_Room, Wards_Ward_ID))
        conn.commit()
        return room



class Room(Resource):
    """This contain all api doing activity with single room"""

    def get(self,Room_ID):
        """retrive a singe room details by its Room_ID"""

        room = conn.execute("SELECT * FROM Rooms WHERE Room_ID=?",(Room_ID,)).fetchall()
        return room


    def delete(self,Room_ID):
        """Delete the room by its Room_ID"""

        conn.execute("DELETE FROM Rooms WHERE Room_ID=?",(Room_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Room_ID):
        """Update the room details by the Room_ID"""

        room = request.get_json(force=True)
        Room_Name = room['Room_Name']
        Availability = room['Availability']
        Cost_of_Room = room['Cost_of_Room']
        Wards_Ward_ID = room['Wards_Ward_ID']
        conn.execute("UPDATE Rooms SET Room_Name=?,Availability=?,Cost_of_Room=?, Wards_Ward_ID=? WHERE Room_ID=?", (Room_Name, Availability, Cost_of_Room, Wards_Ward_ID, Room_ID))
        conn.commit()
        return room