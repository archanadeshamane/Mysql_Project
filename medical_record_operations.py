from db_connection import create_connection

def add_medical_record(patient_id, doctor_id, date_of_record, diagnosis, treatment, medications):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO MedicalRecords (PatientID, DoctorID, DateOfRecord, Diagnosis, Treatment, Medications)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (patient_id, doctor_id, date_of_record, diagnosis, treatment, medications)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def get_medical_record(record_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM MedicalRecords WHERE RecordID = %s"
    cursor.execute(query, (record_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def update_medical_record(record_id, patient_id, doctor_id, date_of_record, diagnosis, treatment, medications):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE MedicalRecords
    SET PatientID = %s, DoctorID = %s, DateOfRecord = %s, Diagnosis = %s, Treatment = %s, Medications = %s
    WHERE RecordID = %s
    """
    values = (patient_id, doctor_id, date_of_record, diagnosis, treatment, medications, record_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def delete_medical_record(record_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM MedicalRecords WHERE RecordID = %s"
    cursor.execute(query, (record_id,))
    connection.commit()
    cursor.close()
    connection.close()
