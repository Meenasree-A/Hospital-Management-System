#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn



class Departments(Resource):
    """This contain apis to carry out activity with all appiontments"""

    def get(self):
        """Retrieve all the departments and return in form of json"""

        # department = conn.execute("SELECT * from department").fetchall()
        department = conn.execute("SELECT * FROM department").fetchall()
        return department

    def post(self):
        """Api to add departments in the database"""

        department = request.get_json(force=True)
        Department_ID = department['Department_ID']
        Department_Name = department['Department_Name']
        conn.execute('''INSERT INTO department(Department_ID, Department_Name) VALUES(?,?)''', (Department_ID, Department_Name))
        conn.commit()
        return department



class Department(Resource):
    """This contains all activities with single department"""

    def get(self,Department_ID):
        """retrive a singe department details by its id"""

        department = conn.execute("SELECT * FROM department WHERE Department_ID=?",(Department_ID,)).fetchall()
        return department


    def put(self,Department_ID):
        """Update the department details by the department id"""

        department = request.get_json(force=True)
        Department_Name = department['Department_Name']
        conn.execute("UPDATE department SET Department_Name=? WHERE Department_ID=?", (Department_Name, Department_ID))
        conn.commit()
        return department