from flask_restful import Resource, Api, request
from package.model import conn



class Appointments(Resource):
    """This contain apis to carry out activity with all appiontments"""

    def get(self):
        """Retrive all the appointment and return in form of json"""

        appointment = conn.execute("SELECT p.*,d.*,a.*,r.* from Appointments a LEFT JOIN patient p ON a.Patient_Patient_ID = p.Patient_ID LEFT JOIN doctor d ON a.Doctor_Doctor_ID = d.Doctor_ID LEFT JOIN Receptionist r ON a.Receptionist_Rep_ID = r.Rep_ID;").fetchall()
        return appointment

    def post(self):
        """Create the appointment by associating patient, doctor and receptionist with appointment date"""

        appointment = request.get_json(force=True)
        Patient_Patient_ID = appointment['Patient_Patient_ID']
        Doctor_Doctor_ID = appointment['Doctor_Doctor_ID']
        Receptionist_Rep_ID = appointment['Receptionist_Rep_ID']
        Appointment_Time = appointment['Appointment_Time']
        appointment['Appointment_ID'] = conn.execute('''INSERT INTO Appointments(Patient_Patient_ID,Doctor_Doctor_ID,Appointment_Time,Receptionist_Rep_ID)
            VALUES(?,?,?,?)''', (Patient_Patient_ID, Doctor_Doctor_ID,Appointment_Time,Receptionist_Rep_ID)).lastrowid
        conn.commit()
        return appointment



class Appointment(Resource):
    """This contain all api doing activity with single appointment"""

    def get(self,Appointment_ID):
        """retrive a singe appointment details by its id"""

        appointment = conn.execute("SELECT * FROM Appointments WHERE Appointment_ID=?",(Appointment_ID,)).fetchall()
        return appointment


    def delete(self,Appointment_ID):
        """Delete the appointment by its id"""

        conn.execute("DELETE FROM Appointments WHERE Appointment_ID=?",(Appointment_ID,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,Appointment_ID):
        """Update the appointment details by the appointment id"""

        appointment = request.get_json(force=True)
        Patient_Patient_ID = appointment['Patient_Patient_ID']
        Doctor_Doctor_ID = appointment['Doctor_Doctor_ID']
        Receptionist_Rep_ID = appointment['Receptionist_Rep_ID']
        conn.execute("UPDATE Appointments SET Patient_Patient_ID=?,Doctor_Doctor_ID=?,Receptionist_Rep_ID=? WHERE Appointment_ID=?",
                     (Patient_Patient_ID, Doctor_Doctor_ID, Receptionist_Rep_ID, Appointment_ID))
        conn.commit()
        return appointment