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
        self._status = AppointmentStatus.SCHEDULED  # protected: no direct external mutation

    @property
    def status(self):
        return self._status

    def cancel(self):
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")
        self._status = AppointmentStatus.CANCELLED

    def complete(self):
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Cannot complete a cancelled appointment")
        if self._status == AppointmentStatus.COMPLETED:
            raise ValueError("Appointment is already completed")
        self._status = AppointmentStatus.COMPLETED

    def check_conflict(self, other: "Appointment") -> bool:
        if other is None:
            raise ValueError("Cannot check conflict against None")
