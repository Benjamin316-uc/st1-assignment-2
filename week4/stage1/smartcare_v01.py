#Task 1

# Simple Python file with basic input, output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = "John Smith"
practitioner1_name = "Dr. Alice Doe"
appointment1_time = "2026-09-04 10:00 AM"

print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = "Bob Johnson"
practitioner2_name = "Dr. Jane Roe"
appointment2_time = "2026-09-04 11:30 AM"

print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")



#tasklenhanced

# Lists, dictionaries and functions to enhance the Pytho file

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time) :
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded")
        return
    for appointment in appointments:
        print(f"Patient: {appointment["patient"]} | Practitioner: {appointment["practitioner"]} | Time: {appointment["time"]}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment("John Smith", "Dr. Alice Doe", "2026-09-04 10:00AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2026-09-04 11:30AM")
display_appointments()


## PART D: AI WRITTEN CODE

# Simple Python example with variables already assigned.
# No database, no GUI — just basic Python.

def store_appointment(patient_name, practitioner_name, appointment_time):
    # Store the appointment in a dictionary
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    return appointment


# Assign values to variables (beginner-friendly)
patient = "Alice Smith"
practitioner = "Dr. John Doe"
appointment_time = "2024-07-20 10:00 AM"

# Call the function
saved_appointment = store_appointment(patient, practitioner, appointment_time)

# Show the result
print(saved_appointment)




