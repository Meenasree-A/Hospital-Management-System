import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'], check_same_thread=False)
conn.execute('pragma foreign_keys=ON')



def dict_factory(cursor, row):
    """This is a function use to format the json when retrieve from the  mysql database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory

conn.execute('''CREATE TABLE if not exists `Department` (
  `Department_ID` INT NOT NULL,
  `Department_Name` VARCHAR(45),
  PRIMARY KEY (`Department_ID`));''')

conn.execute('''CREATE TABLE if not exists `Receptionist` (
  `Rep_ID` INT NOT NULL,
  `Name` VARCHAR(45),
  `SSN` INT,
  `Mobile_Number` INT,
  PRIMARY KEY (`Rep_ID`));''')

conn.execute('''CREATE TABLE if not exists `Medicine`
(`Medicine_ID` INT NOT NULL,
`Medicine_Name` VARCHAR(45),
`Cost` DECIMAL(5),
PRIMARY KEY (`Medicine_ID`));''')

conn.execute('''CREATE TABLE if not exists `Wards` 
(`Ward_ID` INT NOT NULL,
 `Ward_Name` VARCHAR(45),
 PRIMARY KEY (`Ward_ID`));''')

conn.execute('''CREATE TABLE if not exists `Rooms`
(`Room_ID` INT NOT NULL,
  `Room_Name` VARCHAR(45),
  `Availability` VARCHAR(10),
  `Cost_of_Room` DECIMAL(5),
  `Wards_Ward_ID` INT NOT NULL,
  PRIMARY KEY (`Room_ID`, `Wards_Ward_ID`),
  CONSTRAINT `fk_Rooms_Wards1`
    FOREIGN KEY (`Wards_Ward_ID`)
    REFERENCES `Wards` (`Ward_ID`));''')

conn.execute('''CREATE TABLE if not exists `Nurse`
(`Nurse_ID` INT NOT NULL,
 `First_Name` VARCHAR(45),
 `Last_Name` VARCHAR(45),
 `Mobile_Number` VARCHAR(45),
 `SSN` INT,
 `Wards_Ward_ID` INT NOT NULL,
 PRIMARY KEY (`Nurse_ID`),
 CONSTRAINT `fk_Nurse_Wards1`
 FOREIGN KEY (`Wards_Ward_ID`)
 REFERENCES `Wards` (`Ward_ID`));''')

conn.execute('''CREATE TABLE if not exists `Patient_History`
(`Issue_Description` VARCHAR(5) NOT NULL,
 `Visited_Date` DATETIME,
 `Patient_Patient_ID` INT NOT NULL,
 CONSTRAINT `fk_Patient_History_Patient1`
 FOREIGN KEY (`Patient_Patient_ID`)
 REFERENCES `Patient` (`Patient_ID`));''')

conn.execute('''CREATE TABLE  if not exists `Operations`
(`Operation_ID` INT NOT NULL,
`Operation_Name` VARCHAR(45),
`Cost` DECIMAL(5),
`Patient_Patient_ID` INT NOT NULL,
PRIMARY KEY (`Operation_ID`, `Patient_Patient_ID`));''')

conn.execute('''CREATE TABLE if not exists `Medical_Tests`
(`Test_ID` INT NOT NULL,
`Test_Name` VARCHAR(45),
`Test_Cost` DECIMAL(5),
`Patient_Patient_ID` INT NOT NULL,
PRIMARY KEY (`Test_ID`),
CONSTRAINT "fk_Medical_Tests_Patient1" FOREIGN KEY("Patient_Patient_ID") REFERENCES "Patient"("Patient_ID"));''')

conn.execute('''CREATE TABLE if not exists `Reports`
(`Report_ID` INT NOT NULL,
`Name` VARCHAR(45),
`Description` VARCHAR(500),
`Medical_Tests_Test_ID` INT NOT NULL,
`Patient_Patient_ID` INT NOT NULL,
PRIMARY KEY (`Report_ID`, `Patient_Patient_ID`),
CONSTRAINT `fk_Reports_Medical_Tests1`
FOREIGN KEY (`Medical_Tests_Test_ID`)
REFERENCES `Medical_Tests` (`Test_ID`),
CONSTRAINT `fk_Reports_Patient1`
FOREIGN KEY (`Patient_Patient_ID`)
REFERENCES `Patient` (`Patient_ID`));''')

conn.execute('''CREATE TABLE if not exists `Appointments`
(`Appointment_ID` INT NOT NULL,
`Appointment_Time` DATE,
`Receptionist_Rep_ID` INT NOT NULL,
`Patient_Patient_ID` INT NOT NULL,
`Doctor_Doctor_ID` INT NOT NULL,
PRIMARY KEY (`Appointment_ID`, `Patient_Patient_ID`),
CONSTRAINT `fk_Appointments_Receptionist1`
FOREIGN KEY (`Receptionist_Rep_ID`)
REFERENCES `Receptionist` (`Rep_ID`),
CONSTRAINT `fk_Appointments_Patient1`
FOREIGN KEY (`Patient_Patient_ID`)
REFERENCES `Patient` (`Patient_ID`),
CONSTRAINT `fk_Appointments_Doctor1`
FOREIGN KEY (`Doctor_Doctor_ID`)
REFERENCES `Doctor` (`Doctor_ID`));''')

conn.execute('''CREATE TABLE if not exists "Bill" (
"First_Name" TEXT,
"Last_Name"	TEXT,
"Visited_Date" DATE,
"Insurance_ID" INTEGER,
"Operation_Name" TEXT,
"Operation_Cost" INTEGER,
"Test_Name"	INTEGER,
"Test_Cost"	INTEGER
);''')




