class Patient:
    def __init__(self, patient_id: str, name: str, contact_info: str):

        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        if not name: 
            raise ValueError("Patient name cannot be empty")
        if not contact_info:
                    raise ValueError("Contact Information cannot be empty")
        self.patient_id = patient_id
        self.name = name
        self.contact_info = contact_info

    def get_contact_info(self):
        """Return patient's contact information. Not yet implemented."""
        pass
