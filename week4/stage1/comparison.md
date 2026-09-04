Part A - Understand the Problem: AI Off:

The database needs to record the patients name, practitioners name, time of the appointment, whether the appointment has been booked, cancelled or completed

A function to be useful would be to list the affliction in the database so the practioner can be better prepared for the patient. Adding an option for the patient to add any additional information such as allergies or unrelated afflictions may also be useful.  Should include a unique ID for each patient adn practitioner. It would also be useful to instead ask the user to enter the names and time when the code runs to make the system easier to update, perhaps a tuple would be better to create a database that saves over time. 

What could go wrong?
    If there is an issue it may be helpful to inclue the practices contact information. If there is two people with the same name it would be unclear which is which without a unique ID. No conflict check for outside of business hours booking and double-booking.

It is unclear on the appointment duration, operating hours, resolution in the case of double-booking, how many users can access the database at once and what it would look like. Expiry on data or permanent storage of all data?

Part B: Identify Limitations
1. There is no ID for each appointment, making it hard to organise in a large database
2. Do unique patient or practitioner ID leading to confusion in the case of name double ups
3. Nothing is properly saved in the system, meaning that new data will overide the last run of the program, this creates a poor database
4. Without the use of ID numbers or a proper Date/Time system, searching for appointments in the system may be frustrating
5. Time is stored as a string, this means that someone could type anything, something like next week is unclear and will cause confusion over time


Part E: Compare Human and AI Versions

| Question | Human Version | AI Version |
| --- | --- | --- |
| Easy to understand? | Yes | Yes |
| Runs successfully? | Yes | Yes |
| Uses only required features? | Yes | Yes |
| Adds Assumptions? | No | Yes |
| Handles errors? | Yes | Yes |
| Could I explain it? | Yes | Yes | Both display a databse listing the practitioner and patient's name, as well as the time. |

When run, the AI response looks similar, howver, it is not asthetic and does not have options to add muliple different appointments