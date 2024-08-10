from db_connection import create_connection

def add_patient(first_name, last_name, dob, gender, address, phone, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (first_name, last_name, dob, gender, address, phone, email)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    
def get_patient(patient_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Patients WHERE PatientID = %s"
    cursor.execute(query, (patient_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def update_patient(patient_id, first_name, last_name, dob, gender, address, phone, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE Patients
    SET FirstName = %s, LastName = %s, DateOfBirth = %s, Gender = %s, Address = %s, PhoneNumber = %s, Email = %s
    WHERE PatientID = %s
    """
    values = (first_name, last_name, dob, gender, address, phone, email, patient_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def delete_patient(patient_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Patients WHERE PatientID = %s"
    cursor.execute(query, (patient_id,))
    connection.commit()
    cursor.close()
    connection.close()
