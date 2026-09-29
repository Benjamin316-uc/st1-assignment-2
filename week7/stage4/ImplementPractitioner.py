class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):

        if not practitioner_id:
            raise ValueError("Practitioner ID cannot be empty")
        if not name: 
            raise ValueError("Practitioner name cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def get_schedule(self):
        """Return practitioner's schedule. Not yet implemented."""
        pass
