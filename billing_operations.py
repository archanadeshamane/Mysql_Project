from db_connection import create_connection

def add_bill(patient_id, appointment_id, amount, payment_status, date_of_payment):
    connection = create_connection()
    cursor = connection.cursor()
    
    query = """
    INSERT INTO Billing (PatientID, AppointmentID, Amount, PaymentStatus, DateOfPayment)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (patient_id, appointment_id, amount, payment_status, date_of_payment)
    
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def get_bill(bill_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Billing WHERE BillID = %s"
    cursor.execute(query, (bill_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def update_bill(bill_id, patient_id, appointment_id, amount, payment_status, date_of_payment):
    connection = create_connection()
    cursor = connection.cursor()
    query = """
    UPDATE Billing
    SET PatientID = %s, AppointmentID = %s, Amount = %s, PaymentStatus = %s, DateOfPayment = %s
    WHERE BillID = %s
    """
    values = (patient_id, appointment_id, amount, payment_status, date_of_payment, bill_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def delete_bill(bill_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Billing WHERE BillID = %s"
    cursor.execute(query, (bill_id,))
    connection.commit()
    cursor.close()
    connection.close()
