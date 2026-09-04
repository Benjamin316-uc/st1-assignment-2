Part C: Using AI as a tutor

What your code does
Concise takeaway: It prints two hard‑coded appointments, then uses lists, dictionaries, and functions to store and display appointments more flexibly.

Expanded explanation:

The first part simply prints two appointment records using variables and f‑strings.

The enhanced section introduces:

* A list called appointments to store multiple appointment entries.

* A function book_appointment() that:

    * Validates the patient name.

    * Creates a dictionary with patient, practitioner, and time.

    * Appends that dictionary to the appointments list.

* A function display_appointments() that:

    * Prints all stored appointments in a loop.

* Finally, you call the functions to add two appointments and display them.

Overall, it’s a small, procedural appointment‑booking demo using basic Python structures.

2. Three limitations
Here are three meaningful constraints in your current design:

No persistence: All appointments disappear when the program ends because everything is stored in memory only.

No input from the user: The program prints fixed values; it doesn’t allow interactive booking.

No conflict checking: You can book multiple appointments at the same time with the same practitioner — the system doesn’t prevent double‑booking.

3. Suggested improvements
Without rewriting your application, here are targeted enhancements:

* Add user input  
Let users type patient names, practitioner names, and times instead of hard‑coding values.

* Add validation rules  
* For example:

    * Prevent empty practitioner names.

    * Check for overlapping appointments.

    * Ensure time formats are valid.

* Introduce simple persistence  
Save appointments to a text file or JSON file so the data survives after the program closes.

These improvements keep your structure but make the system more realistic and robust.

4. Two questions to test your understanding
    1. Why is a dictionary a good data structure for storing each appointment?

    2. What would happen if you called display_appointments() before booking any appointments?


Part F: Verify the behaviour

A normal appointment displays well and runs as expected

a blank patient name does not break the code however returns as:
    'patient': '', 'practitioner': 'Dr. John Doe', 'time': '2024-07-20 10:00 AM'
This makes it unclear who the patient is

Having two appointments for the same practitioner/time is non-applicable in this case as the AI did not generate options for appointments. However in the case that different names are applyed to the practitioner/time variable, it would display both in the same appointment. 

In the case that there is strange inputs such as  patient=None or time=None. The system allows this. This is expected for the patient variable, however in a system string value should not be allowed in the time variable, this is a change that would have to be made.


Part G: Improve one thing

Change the time string into a datetime answer. For example:

from datetime import datetime

appointment_time = datetime.strptime('2024-07-20 10:00 AM', '%Y-%m-%d %I:%M %p')

then,

saved_appointment = store_appointment(patient, practitioner, appointment_time.strftime('%Y-%m-%d %I:%M %p'))

to convert it back to a nice readable string.