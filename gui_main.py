import tkinter as tk
from tkinter import ttk, messagebox
from patient_operations import add_patient, get_patient, update_patient, delete_patient
from doctor_operations import add_doctor, get_doctor, update_doctor, delete_doctor
from appointment_operations import add_appointment, get_appointment, update_appointment, delete_appointment
from medical_record_operations import add_medical_record, get_medical_record, update_medical_record, delete_medical_record
from billing_operations import add_bill, get_bill, update_bill, delete_bill
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("EHR System")

tab_control = ttk.Notebook(root)

# Define tabs
patient_tab = ttk.Frame(tab_control)
doctor_tab = ttk.Frame(tab_control)
appointment_tab = ttk.Frame(tab_control)
medical_record_tab = ttk.Frame(tab_control)
billing_tab = ttk.Frame(tab_control)

tab_control.add(patient_tab, text="Patients")
tab_control.add(doctor_tab, text="Doctors")
tab_control.add(appointment_tab, text="Appointments")
tab_control.add(medical_record_tab, text="Medical Records")
tab_control.add(billing_tab, text="Billing")

tab_control.pack(expand=1, fill="both")

# Utility functions
def clear_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)
    gender_var.set('')
    payment_status_var.set('')
    
# Function to validate amount
def validate_amount(amount_str):
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

# Patient Tab
def add_patient_gui():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    try:
        add_patient(first_name, last_name, dob, gender, address, phone, email)
        messagebox.showinfo("Success", "Patient added successfully")
        clear_entries([first_name_entry, last_name_entry, dob_entry, address_entry, phone_entry, email_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_patient_gui():
    patient_id = patient_id_entry.get()
    try:
        result = get_patient(patient_id)
        if result:
            first_name_entry.delete(0, tk.END)
            first_name_entry.insert(0, result[1])
            last_name_entry.delete(0, tk.END)
            last_name_entry.insert(0, result[2])
            dob_entry.delete(0, tk.END)
            dob_entry.insert(0, result[3])
            gender_var.set(result[4])
            address_entry.delete(0, tk.END)
            address_entry.insert(0, result[5])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, result[6])
            email_entry.delete(0, tk.END)
            email_entry.insert(0, result[7])
        else:
            messagebox.showinfo("Not Found", "Patient not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_patient_gui():
    patient_id = patient_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    try:
        update_patient(patient_id, first_name, last_name, dob, gender, address, phone, email)
        messagebox.showinfo("Success", "Patient updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_patient_gui():
    patient_id = patient_id_entry.get()
    try:
        delete_patient(patient_id)
        messagebox.showinfo("Success", "Patient deleted successfully")
        clear_entries([first_name_entry, last_name_entry, dob_entry, address_entry, phone_entry, email_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Patient Form Fields
tk.Label(patient_tab, text="Patient ID").grid(column=0, row=0)
patient_id_entry = tk.Entry(patient_tab)
patient_id_entry.grid(column=1, row=0)

tk.Label(patient_tab, text="First Name").grid(column=0, row=1)
first_name_entry = tk.Entry(patient_tab)
first_name_entry.grid(column=1, row=1)

tk.Label(patient_tab, text="Last Name").grid(column=0, row=2)
last_name_entry = tk.Entry(patient_tab)
last_name_entry.grid(column=1, row=2)

tk.Label(patient_tab, text="Date of Birth").grid(column=0, row=3)
dob_entry = tk.Entry(patient_tab)
dob_entry.grid(column=1, row=3)

tk.Label(patient_tab, text="Gender").grid(column=0, row=4)
gender_var = tk.StringVar()
tk.Radiobutton(patient_tab, text="Male", variable=gender_var, value="Male").grid(column=1, row=4)
tk.Radiobutton(patient_tab, text="Female", variable=gender_var, value="Female").grid(column=2, row=4)
tk.Radiobutton(patient_tab, text="Other", variable=gender_var, value="Other").grid(column=3, row=4)

tk.Label(patient_tab, text="Address").grid(column=0, row=5)
address_entry = tk.Entry(patient_tab)
address_entry.grid(column=1, row=5)

tk.Label(patient_tab, text="Phone Number").grid(column=0, row=6)
phone_entry = tk.Entry(patient_tab)
phone_entry.grid(column=1, row=6)

tk.Label(patient_tab, text="Email").grid(column=0, row=7)
email_entry = tk.Entry(patient_tab)
email_entry.grid(column=1, row=7)

tk.Button(patient_tab, text="Add Patient", command=add_patient_gui).grid(column=0, row=8)
tk.Button(patient_tab, text="Get Patient", command=get_patient_gui).grid(column=1, row=8)
tk.Button(patient_tab, text="Update Patient", command=update_patient_gui).grid(column=2, row=8)
tk.Button(patient_tab, text="Delete Patient", command=delete_patient_gui).grid(column=3, row=8)

# Doctor Tab
def add_doctor_gui():
    first_name = doctor_first_name_entry.get()
    last_name = doctor_last_name_entry.get()
    specialization = doctor_specialization_entry.get()
    phone = doctor_phone_entry.get()
    email = doctor_email_entry.get()
    try:
        add_doctor(first_name, last_name, specialization, phone, email)
        messagebox.showinfo("Success", "Doctor added successfully")
        clear_entries([doctor_first_name_entry, doctor_last_name_entry, doctor_specialization_entry, doctor_phone_entry, doctor_email_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_doctor_gui():
    doctor_id = doctor_id_entry.get()
    try:
        result = get_doctor(doctor_id)
        if result:
            doctor_first_name_entry.delete(0, tk.END)
            doctor_first_name_entry.insert(0, result[1])
            doctor_last_name_entry.delete(0, tk.END)
            doctor_last_name_entry.insert(0, result[2])
            doctor_specialization_entry.delete(0, tk.END)
            doctor_specialization_entry.insert(0, result[3])
            doctor_phone_entry.delete(0, tk.END)
            doctor_phone_entry.insert(0, result[4])
            doctor_email_entry.delete(0, tk.END)
            doctor_email_entry.insert(0, result[5])
        else:
            messagebox.showinfo("Not Found", "Doctor not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_doctor_gui():
    doctor_id = doctor_id_entry.get()
    first_name = doctor_first_name_entry.get()
    last_name = doctor_last_name_entry.get()
    specialization = doctor_specialization_entry.get()
    phone = doctor_phone_entry.get()
    email = doctor_email_entry.get()
    try:
        update_doctor(doctor_id, first_name, last_name, specialization, phone, email)
        messagebox.showinfo("Success", "Doctor updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_doctor_gui():
    doctor_id = doctor_id_entry.get()
    try:
        delete_doctor(doctor_id)
        messagebox.showinfo("Success", "Doctor deleted successfully")
        clear_entries([doctor_first_name_entry, doctor_last_name_entry, doctor_specialization_entry, doctor_phone_entry, doctor_email_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Doctor Form Fields
tk.Label(doctor_tab, text="Doctor ID").grid(column=0, row=0)
doctor_id_entry = tk.Entry(doctor_tab)
doctor_id_entry.grid(column=1, row=0)

tk.Label(doctor_tab, text="First Name").grid(column=0, row=1)
doctor_first_name_entry = tk.Entry(doctor_tab)
doctor_first_name_entry.grid(column=1, row=1)

tk.Label(doctor_tab, text="Last Name").grid(column=0, row=2)
doctor_last_name_entry = tk.Entry(doctor_tab)
doctor_last_name_entry.grid(column=1, row=2)

tk.Label(doctor_tab, text="Specialization").grid(column=0, row=3)
doctor_specialization_entry = tk.Entry(doctor_tab)
doctor_specialization_entry.grid(column=1, row=3)

tk.Label(doctor_tab, text="Phone Number").grid(column=0, row=4)
doctor_phone_entry = tk.Entry(doctor_tab)
doctor_phone_entry.grid(column=1, row=4)

tk.Label(doctor_tab, text="Email").grid(column=0, row=5)
doctor_email_entry = tk.Entry(doctor_tab)
doctor_email_entry.grid(column=1, row=5)

tk.Button(doctor_tab, text="Add Doctor", command=add_doctor_gui).grid(column=0, row=6)
tk.Button(doctor_tab, text="Get Doctor", command=get_doctor_gui).grid(column=1, row=6)
tk.Button(doctor_tab, text="Update Doctor", command=update_doctor_gui).grid(column=2, row=6)
tk.Button(doctor_tab, text="Delete Doctor", command=delete_doctor_gui).grid(column=3, row=6)

# Appointment Tab
def add_appointment_gui():
    patient_id = appointment_patient_id_entry.get()
    doctor_id = appointment_doctor_id_entry.get()
    appointment_date = appointment_date_entry.get()
    reason = appointment_reason_entry.get()
    try:
        add_appointment(patient_id, doctor_id, appointment_date, reason)
        messagebox.showinfo("Success", "Appointment added successfully")
        clear_entries([appointment_patient_id_entry, appointment_doctor_id_entry, appointment_date_entry, appointment_reason_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_appointment_gui():
    appointment_id = appointment_id_entry.get()
    try:
        result = get_appointment(appointment_id)
        if result:
            appointment_patient_id_entry.delete(0, tk.END)
            appointment_patient_id_entry.insert(0, result[1])
            appointment_doctor_id_entry.delete(0, tk.END)
            appointment_doctor_id_entry.insert(0, result[2])
            appointment_date_entry.delete(0, tk.END)
            appointment_date_entry.insert(0, result[3])
            appointment_reason_entry.delete(0, tk.END)
            appointment_reason_entry.insert(0, result[4])
        else:
            messagebox.showinfo("Not Found", "Appointment not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_appointment_gui():
    appointment_id = appointment_id_entry.get()
    patient_id = appointment_patient_id_entry.get()
    doctor_id = appointment_doctor_id_entry.get()
    appointment_date = appointment_date_entry.get()
    reason = appointment_reason_entry.get()
    try:
        update_appointment(appointment_id, patient_id, doctor_id, appointment_date, reason)
        messagebox.showinfo("Success", "Appointment updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_appointment_gui():
    appointment_id = appointment_id_entry.get()
    try:
        delete_appointment(appointment_id)
        messagebox.showinfo("Success", "Appointment deleted successfully")
        clear_entries([appointment_patient_id_entry, appointment_doctor_id_entry, appointment_date_entry, appointment_reason_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Appointment Form Fields
tk.Label(appointment_tab, text="Appointment ID").grid(column=0, row=0)
appointment_id_entry = tk.Entry(appointment_tab)
appointment_id_entry.grid(column=1, row=0)

tk.Label(appointment_tab, text="Patient ID").grid(column=0, row=1)
appointment_patient_id_entry = tk.Entry(appointment_tab)
appointment_patient_id_entry.grid(column=1, row=1)

tk.Label(appointment_tab, text="Doctor ID").grid(column=0, row=2)
appointment_doctor_id_entry = tk.Entry(appointment_tab)
appointment_doctor_id_entry.grid(column=1, row=2)

tk.Label(appointment_tab, text="Appointment Date").grid(column=0, row=3)
appointment_date_entry = tk.Entry(appointment_tab)
appointment_date_entry.grid(column=1, row=3)

tk.Label(appointment_tab, text="Reason for Visit").grid(column=0, row=4)
appointment_reason_entry = tk.Entry(appointment_tab)
appointment_reason_entry.grid(column=1, row=4)

tk.Button(appointment_tab, text="Add Appointment", command=add_appointment_gui).grid(column=0, row=5)
tk.Button(appointment_tab, text="Get Appointment", command=get_appointment_gui).grid(column=1, row=5)
tk.Button(appointment_tab, text="Update Appointment", command=update_appointment_gui).grid(column=2, row=5)
tk.Button(appointment_tab, text="Delete Appointment", command=delete_appointment_gui).grid(column=3, row=5)

# Medical Records Tab
def add_medical_record_gui():
    patient_id = record_patient_id_entry.get()
    doctor_id = record_doctor_id_entry.get()
    date_of_record = record_date_entry.get()
    diagnosis = record_diagnosis_entry.get()
    treatment = record_treatment_entry.get()
    medications = record_medications_entry.get()
    try:
        add_medical_record(patient_id, doctor_id, date_of_record, diagnosis, treatment, medications)
        messagebox.showinfo("Success", "Medical Record added successfully")
        clear_entries([record_patient_id_entry, record_doctor_id_entry, record_date_entry, record_diagnosis_entry, record_treatment_entry, record_medications_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_medical_record_gui():
    record_id = record_id_entry.get()
    try:
        result = get_medical_record(record_id)
        if result:
            record_patient_id_entry.delete(0, tk.END)
            record_patient_id_entry.insert(0, result[1])
            record_doctor_id_entry.delete(0, tk.END)
            record_doctor_id_entry.insert(0, result[2])
            record_date_entry.delete(0, tk.END)
            record_date_entry.insert(0, result[3])
            record_diagnosis_entry.delete(0, tk.END)
            record_diagnosis_entry.insert(0, result[4])
            record_treatment_entry.delete(0, tk.END)
            record_treatment_entry.insert(0, result[5])
            record_medications_entry.delete(0, tk.END)
            record_medications_entry.insert(0, result[6])
        else:
            messagebox.showinfo("Not Found", "Medical Record not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_medical_record_gui():
    record_id = record_id_entry.get()
    patient_id = record_patient_id_entry.get()
    doctor_id = record_doctor_id_entry.get()
    date_of_record = record_date_entry.get()
    diagnosis = record_diagnosis_entry.get()
    treatment = record_treatment_entry.get()
    medications = record_medications_entry.get()
    try:
        update_medical_record(record_id, patient_id, doctor_id, date_of_record, diagnosis, treatment, medications)
        messagebox.showinfo("Success", "Medical Record updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_medical_record_gui():
    record_id = record_id_entry.get()
    try:
        delete_medical_record(record_id)
        messagebox.showinfo("Success", "Medical Record deleted successfully")
        clear_entries([record_patient_id_entry, record_doctor_id_entry, record_date_entry, record_diagnosis_entry, record_treatment_entry, record_medications_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Medical Records Form Fields
tk.Label(medical_record_tab, text="Record ID").grid(column=0, row=0)
record_id_entry = tk.Entry(medical_record_tab)
record_id_entry.grid(column=1, row=0)

tk.Label(medical_record_tab, text="Patient ID").grid(column=0, row=1)
record_patient_id_entry = tk.Entry(medical_record_tab)
record_patient_id_entry.grid(column=1, row=1)

tk.Label(medical_record_tab, text="Doctor ID").grid(column=0, row=2)
record_doctor_id_entry = tk.Entry(medical_record_tab)
record_doctor_id_entry.grid(column=1, row=2)

tk.Label(medical_record_tab, text="Date of Record").grid(column=0, row=3)
record_date_entry = tk.Entry(medical_record_tab)
record_date_entry.grid(column=1, row=3)

tk.Label(medical_record_tab, text="Diagnosis").grid(column=0, row=4)
record_diagnosis_entry = tk.Entry(medical_record_tab)
record_diagnosis_entry.grid(column=1, row=4)

tk.Label(medical_record_tab, text="Treatment").grid(column=0, row=5)
record_treatment_entry = tk.Entry(medical_record_tab)
record_treatment_entry.grid(column=1, row=5)

tk.Label(medical_record_tab, text="Medications").grid(column=0, row=6)
record_medications_entry = tk.Entry(medical_record_tab)
record_medications_entry.grid(column=1, row=6)

tk.Button(medical_record_tab, text="Add Medical Record", command=add_medical_record_gui).grid(column=0, row=7)
tk.Button(medical_record_tab, text="Get Medical Record", command=get_medical_record_gui).grid(column=1, row=7)
tk.Button(medical_record_tab, text="Update Medical Record", command=update_medical_record_gui).grid(column=2, row=7)
tk.Button(medical_record_tab, text="Delete Medical Record", command=delete_medical_record_gui).grid(column=3, row=7)

# Billing Tab
def add_bill_gui():
    try:
        patient_id = bill_patient_id_entry.get()
        appointment_id = bill_appointment_id_entry.get()
        amount_str = bill_amount_entry.get()
        payment_status = payment_status_var.get()
        date_of_payment = bill_date_entry.get()

        if not validate_amount(amount_str):
            messagebox.showerror("Error", "Invalid amount format. Please enter a valid decimal number.")
            return

        amount_decimal = float(amount_str)
        add_bill(patient_id, appointment_id, amount_decimal, payment_status, date_of_payment)
        messagebox.showinfo("Success", "Bill added successfully")
        clear_entries([bill_id_entry, bill_patient_id_entry, bill_appointment_id_entry, bill_amount_entry, bill_date_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_bill_gui():
    try:
        bill_id = bill_id_entry.get()
        bill_details = get_bill(bill_id)
        if bill_details:
            bill_patient_id_entry.delete(0, tk.END)
            bill_patient_id_entry.insert(0, bill_details[1])
            bill_appointment_id_entry.delete(0, tk.END)
            bill_appointment_id_entry.insert(0, bill_details[2])
            bill_amount_entry.delete(0, tk.END)
            bill_amount_entry.insert(0, bill_details[3])
            payment_status_var.set(bill_details[4])
            bill_date_entry.delete(0, tk.END)
            bill_date_entry.insert(0, bill_details[5])
        else:
            messagebox.showinfo("Info", "Bill not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_bill_gui():
    try:
        bill_id = bill_id_entry.get()
        patient_id = bill_patient_id_entry.get()
        appointment_id = bill_appointment_id_entry.get()
        amount_str = bill_amount_entry.get()
        payment_status = payment_status_var.get()
        date_of_payment = bill_date_entry.get()

        if not validate_amount(amount_str):
            messagebox.showerror("Error", "Invalid amount format. Please enter a valid decimal number.")
            return

        amount_decimal = float(amount_str)
        update_bill(bill_id, patient_id, appointment_id, amount_decimal, payment_status, date_of_payment)
        messagebox.showinfo("Success", "Bill updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_bill_gui():
    try:
        bill_id = bill_id_entry.get()
        delete_bill(bill_id)
        messagebox.showinfo("Success", "Bill deleted successfully")
        clear_entries([bill_id_entry, bill_patient_id_entry, bill_appointment_id_entry, bill_amount_entry, bill_date_entry])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Billing Form Fields
# Billing Form Fields
tk.Label(billing_tab, text="Bill ID").grid(column=0, row=0)
bill_id_entry = tk.Entry(billing_tab)
bill_id_entry.grid(column=1, row=0)

tk.Label(billing_tab, text="Patient ID").grid(column=0, row=1)
bill_patient_id_entry = tk.Entry(billing_tab)
bill_patient_id_entry.grid(column=1, row=1)

tk.Label(billing_tab, text="Appointment ID").grid(column=0, row=2)
bill_appointment_id_entry = tk.Entry(billing_tab)
bill_appointment_id_entry.grid(column=1, row=2)

tk.Label(billing_tab, text="Amount").grid(column=0, row=3)
bill_amount_entry = tk.Entry(billing_tab)
bill_amount_entry.grid(column=1, row=3)

tk.Label(billing_tab, text="Payment Status").grid(column=0, row=4)
payment_status_var = tk.StringVar()
tk.Radiobutton(billing_tab, text="Paid", variable=payment_status_var, value="Paid").grid(column=1, row=4)
tk.Radiobutton(billing_tab, text="Unpaid", variable=payment_status_var, value="Unpaid").grid(column=2, row=4)

tk.Label(billing_tab, text="Date of Payment").grid(column=0, row=5)
bill_date_entry = tk.Entry(billing_tab)
bill_date_entry.grid(column=1, row=5)

tk.Button(billing_tab, text="Add Bill", command=add_bill_gui).grid(column=0, row=6)
tk.Button(billing_tab, text="Get Bill", command=get_bill_gui).grid(column=1, row=6)
tk.Button(billing_tab, text="Update Bill", command=update_bill_gui).grid(column=2, row=6)
tk.Button(billing_tab, text="Delete Bill", command=delete_bill_gui).grid(column=3, row=6)



root.mainloop()
