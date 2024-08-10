from db_connection import create_connection

def add_appointment(patient_id, doctor_id, appointment_date, reason):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, ReasonForVisit)
    VALUES (%s, %s, %s, %s)
    """
    values = (patient_id, doctor_id, appointment_date, reason)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def get_appointment(appointment_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Appointments WHERE AppointmentID = %s"
    cursor.execute(query, (appointment_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def update_appointment(appointment_id, patient_id, doctor_id, appointment_date, reason):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE Appointments
    SET PatientID = %s, DoctorID = %s, AppointmentDate = %s, ReasonForVisit = %s
    WHERE AppointmentID = %s
    """
    values = (patient_id, doctor_id, appointment_date, reason, appointment_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def delete_appointment(appointment_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Appointments WHERE AppointmentID = %s"
    cursor.execute(query, (appointment_id,))
    connection.commit()
    cursor.close()
    connection.close()
