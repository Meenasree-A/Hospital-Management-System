from flask_restful import Resource, Api, request
from package.model import conn


class Common(Resource):
    """This contain common api ie noe related to the specific module"""

    def get(self):
        """Retrieve the count for the dashboard page"""

        getPatientCount=conn.execute("SELECT COUNT(*) AS patient FROM patient").fetchone()
        getDoctorCount = conn.execute("SELECT COUNT(*) AS doctor FROM doctor").fetchone()
        getAppointmentCount = conn.execute("SELECT COUNT(*) AS appointment FROM Appointments").fetchone()
        getReceptionistCount = conn.execute("SELECT COUNT(*) AS receptionist FROM receptionist").fetchone()
        getMedicationCount = conn.execute("SELECT COUNT(*) AS medication from Medicine").fetchone()
        getDepartmentCount = conn.execute("SELECT COUNT(*) AS department FROM department").fetchone()
        getNurseCount = conn.execute("SELECT COUNT(*) AS nurse FROM nurse").fetchone()
        getRoomCount = conn.execute("SELECT COUNT(*) AS room FROM rooms").fetchone()
        getProcedureCount = conn.execute("SELECT COUNT(*) AS operation FROM Operations").fetchone()
        getWardsCount = conn.execute("SELECT COUNT(*) AS wards FROM Wards").fetchone()
        getPatienthistoryCount = conn.execute("SELECT COUNT(*) AS patienthistories FROM Patient_History").fetchone()
        getMedicaltestCount = conn.execute("SELECT COUNT(*) AS medicaltest FROM Medical_Tests").fetchone()
        getReportCount = conn.execute("SELECT COUNT(*) AS report FROM Reports").fetchone()
        getBillCount = conn.execute("SELECT COUNT(*) AS bill FROM Bill").fetchone()

        getPatientCount.update(getDoctorCount)
        getPatientCount.update(getAppointmentCount)
        getPatientCount.update(getReceptionistCount)
        getPatientCount.update(getMedicationCount)
        getPatientCount.update(getDepartmentCount)
        getPatientCount.update(getNurseCount)
        getPatientCount.update(getRoomCount)
        getPatientCount.update(getProcedureCount)
        getPatientCount.update(getWardsCount)
        getPatientCount.update(getPatienthistoryCount)
        getPatientCount.update(getMedicaltestCount)
        getPatientCount.update(getReportCount)
        getPatientCount.update(getBillCount)

        return getPatientCount