from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class Appointment:
    def __init__(self, appointment_id: str, patient, practitioner, time: datetime):
        if not appointment_id:
            raise ValueError("Appointment ID cannot be empty")
        if patient is None:
            raise ValueError("Appointment must have a patient")
        if practitioner is None:
            raise ValueError("Appointment must have a practitioner")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = AppointmentStatus.SCHEDULED

    def cancel(self):
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")
        self.status = AppointmentStatus.CANCELLED

    def complete(self):
        self.status = AppointmentStatus.COMPLETED

    def check_conflict(self, other: "Appointment") -> bool:
        if self.practitioner != other.practitioner:
            return False
        return self.time == other.time
