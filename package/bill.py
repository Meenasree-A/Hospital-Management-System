from flask_restful import Resource, Api, request
from package.model import conn



class bills(Resource):

    def get(self):
        """Retrieve all the bill and return in form of json"""
        conn.execute("DELETE FROM BILL")
        conn.execute("INSERT INTO Bill SELECT p.First_Name, p.Last_Name, ph.Visited_Date, p.Insurance_ID, o.Operation_Name, o.cost, mt.Test_Name, mt.Test_Cost FROM Patient_History ph LEFT JOIN Operations o ON ph.Patient_Patient_ID = o.Patient_Patient_ID LEFT JOIN Medical_Tests mt ON ph.Patient_Patient_ID = mt.Patient_Patient_ID LEFT JOIN Patient p ON ph.Patient_Patient_ID = p.Patient_ID;")
        conn.commit()
        bill = conn.execute("SELECT * FROM BILL").fetchall()
        
        return bill
