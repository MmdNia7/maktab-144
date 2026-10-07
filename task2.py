import re
from datetime import datetime,timedelta
import argparse



class Doctor:
    def __init__(self,id,name,special,medical_license_number,email):
        if re.match(r"^DOC-\d{3}$",id):
            self.id = id
        else:
            raise ValueError("Invalid doctor id")
        self.name = name
        self.special = special  
        if re.match(r"^\d{6}$",medical_license_number):  
            self.medical_license_number = medical_license_number
        else:
            raise  ValueError("Invalid medical license number")    
        self.email = email

    @property
    def display_name(self):
        return self.name + " | " + self.special


class Patient:
    def __init__(self, id, name, birth_date, national_code, phone_number):
        if re.match(r"^PAT-\d{5}$", id):
            self.id = id
        else:
            raise ValueError("Invalid patient id")
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
        if re.match(r"^\d{10}$", national_code):
            self.national_code = national_code
        else:
            raise ValueError("Invalid national code")
        self.phone_number = phone_number

    @property
    def age(self):
        today = datetime.now()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


class Appointment:
    def __init__(
        self,
        id,
        doctor_id,
        patient_id,
        appointment_datetime,
        duration,
        status,
        note
    ):
        if re.match(r"^APT-\d{8}-\d{3}", id):
            self.id = id
        else:
            raise ValueError("Invalid appointment id")

        self.doctor_id = doctor_id
        self.patient_id = patient_id

        self.appointment_datetime = datetime.strptime(
            appointment_datetime,
            "%Y-%m-%d %H:%M"
        )

        if self.appointment_datetime <= datetime.now():
            raise ValueError("Appointment must be in the future")

        self.duration = duration

        if status in ["scheduled", "done", "cancelled", "no-show"]:
            self.status = status
        else:
            raise ValueError("Invalid appointment status")

        self.note = note

    @property
    def time_end(self):
        return self.appointment_datetime + timedelta(minutes=self.duration)    


class ClinicSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        for d in self.doctors:
            if d.id == doctor.id:
                raise ValueError("This doctor has already been registered.")
        self.doctors.append(doctor)

    def add_patient(self, patient):
        for p in self.patients:
            if p.id == patient.id:
                raise ValueError("This patient has already been registered.")
        self.patients.append(patient)    

    def remove_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                self.doctors.remove(doctor)
                return

        raise ValueError("Doctor not found")


    def remove_patient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for appointment in self.appointments:
                    if (
                        appointment.patient_id == patient_id
                        and appointment.appointment_datetime > datetime.now()
                    ):
                        raise ValueError("Cannot remove patient with a future appointment")

                self.patients.remove(patient)
                return
        raise ValueError("Patient not found")


    def doctor_daily_schedule(self, doctor_id, date):
        appointments = []

        for appointment in self.appointments:
            if (
                appointment.doctor_id == doctor_id
                and appointment.appointment_datetime.date() == date.date()
            ):
                appointments.append(appointment)

        appointments.sort(
            key=lambda appointment: appointment.appointment_datetime
        )
        return appointments


    def monthly_stats(self, year, month):
        result = []
        for doctor in self.doctors:
            done = 0
            cancelled = 0
            no_show = 0

            for appointment in self.appointments:
                if (
                    appointment.doctor_id == doctor.id
                    and appointment.appointment_datetime.year == year
                    and appointment.appointment_datetime.month == month
                ):
                    if appointment.status == "done":
                        done += 1
                    elif appointment.status == "cancelled":
                        cancelled += 1
                    elif appointment.status == "no-show":
                        no_show += 1

            result.append(
                (
                doctor.name,
                "done:", done,
                "cancelled:", cancelled,
                "no-show:", no_show
                )
            )    
        return result    


doctor1 = Doctor(
    "DOC-001",
    "Milad Kor",
    "Cardiologist",
    "123456",
    "ali@example.com"
)

doctor2 = Doctor(
    "DOC-002",
    "Ramin Nosrati",
    "Neurologist",
    "234567",
    "reza@example.com"
)

doctor3 = Doctor(
    "DOC-003",
    "Asra Pahlevan",
    "Dermatologist",
    "345678",
    "sara@example.com"
)


patient1 = Patient(
    "PAT-00001",
    "Mohammad",
    "15-05-2000",
    "1234567890",
    "09121234567"
)

patient2 = Patient(
    "PAT-00002",
    "Ali",
    "20-08-1998",
    "2345678901",
    "09129876543"
)

patient3 = Patient(
    "PAT-00003",
    "Reza",
    "10-01-2002",
    "3456789012",
    "09121112233"
)

patient4 = Patient(
    "PAT-00004",
    "Sara",
    "25-11-1995",
    "4567890123",
    "09123334455"
)

patient5 = Patient(
    "PAT-00005",
    "Zahra",
    "05-03-2001",
    "5678901234",
    "09125556677"
)


clinic = ClinicSystem()

clinic.add_doctor(doctor1)
clinic.add_doctor(doctor2)
clinic.add_doctor(doctor3)

clinic.add_patient(patient1)
clinic.add_patient(patient2)
clinic.add_patient(patient3)
clinic.add_patient(patient4)
clinic.add_patient(patient5)


appointment1 = Appointment(
    "APT-20261010-001",
    "DOC-001",
    "PAT-00001",
    "2026-10-10 09:00",
    30,
    "scheduled",
    "First visit"
)

appointment2 = Appointment(
    "APT-20261010-002",
    "DOC-001",
    "PAT-00002",
    "2026-10-10 10:00",
    45,
    "done",
    "Regular checkup"
)

appointment3 = Appointment(
    "APT-20261011-003",
    "DOC-002",
    "PAT-00003",
    "2026-10-11 11:00",
    30,
    "cancelled",
    "Patient cancelled"
)

appointment4 = Appointment(
    "APT-20261011-004",
    "DOC-002",
    "PAT-00004",
    "2026-10-11 13:00",
    60,
    "scheduled",
    "Neurology consultation"
)

appointment5 = Appointment(
    "APT-20261012-005",
    "DOC-003",
    "PAT-00005",
    "2026-10-12 09:30",
    30,
    "done",
    "Skin examination"
)

appointment6 = Appointment(
    "APT-20261012-006",
    "DOC-003",
    "PAT-00001",
    "2026-10-12 11:00",
    45,
    "no-show",
    "Patient did not arrive"
)

appointment7 = Appointment(
    "APT-20261013-007",
    "DOC-001",
    "PAT-00003",
    "2026-10-13 14:00",
    30,
    "scheduled",
    "Follow-up"
)

appointment8 = Appointment(
    "APT-20261014-008",
    "DOC-002",
    "PAT-00005",
    "2026-10-14 16:00",
    45,
    "done",
    "Final consultation"
)

clinic.appointments.append(appointment1)
clinic.appointments.append(appointment2)
clinic.appointments.append(appointment3)
clinic.appointments.append(appointment4)
clinic.appointments.append(appointment5)
clinic.appointments.append(appointment6)
clinic.appointments.append(appointment7)
clinic.appointments.append(appointment8)



# CLI


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

doctors_parser = subparsers.add_parser("doctors-list")
doctors_parser.add_argument("--specialty")

patients_parser = subparsers.add_parser("patients-list")
patients_parser.add_argument("--name")

schedule_parser = subparsers.add_parser("schedule-doctor")
schedule_parser.add_argument("--doctor-id", required=True)
schedule_parser.add_argument("--date", required=True)

stats_parser = subparsers.add_parser("monthly-stats")
stats_parser.add_argument("--month", required=True)


args = parser.parse_args()


if args.command == "doctors-list":

    for doctor in clinic.doctors:

        if args.specialty:
            if doctor.special != args.specialty:
                continue

        print(doctor.display_name)


elif args.command == "patients-list":

    for patient in clinic.patients:

        if args.name:
            if not re.search(args.name, patient.name, re.IGNORECASE):
                continue

        print(patient.name)


elif args.command == "schedule-doctor":

    date = datetime.strptime(args.date, "%d-%m-%Y")

    appointments = clinic.doctor_daily_schedule(
        args.doctor_id,
        date
    )

    for appointment in appointments:
        print(
            appointment.id,
            appointment.appointment_datetime,
            appointment.patient_id,
            appointment.status
        )


elif args.command == "monthly-stats":

    month = datetime.strptime(args.month, "%Y-%m")

    result = clinic.monthly_stats(
        month.year,
        month.month
    )

    print(result)