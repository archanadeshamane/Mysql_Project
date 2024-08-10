from db_connection import create_connection

def add_doctor(first_name, last_name, specialization, phone, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO Doctors (FirstName, LastName, Specialization, PhoneNumber, Email)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (first_name, last_name, specialization, phone, email)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    
def get_doctor(doctor_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Doctors WHERE DoctorID = %s"
    cursor.execute(query, (doctor_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def update_doctor(doctor_id, first_name, last_name, specialization, phone, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE Doctors
    SET FirstName = %s, LastName = %s, Specialization = %s, PhoneNumber = %s, Email = %s
    WHERE DoctorID = %s
    """
    values = (first_name, last_name, specialization, phone, email, doctor_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def delete_doctor(doctor_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Doctors WHERE DoctorID = %s"
    cursor.execute(query, (doctor_id,))
    connection.commit()
    cursor.close()
    connection.close()
