from django.core.management.base import BaseCommand
from api.models import Doctor, Appointment
from datetime import date

class Command(BaseCommand):
    help = 'Seed database with sample doctors and appointments'

    def handle(self, *args, **kwargs):
        doctor1 = Doctor.objects.create(name="Dr. Vivek", specialization="Cardiology")
        doctor2 = Doctor.objects.create(name="Dr. Akhil", specialization="Dermatology")

        Appointment.objects.create(patient_name="Shivam", doctor=doctor1, date=date.today(), time_slot="10:00 AM", status="Scheduled")
        Appointment.objects.create(patient_name="Aryan", doctor=doctor2, date=date.today(), time_slot="11:30 AM", status="Completed")

        self.stdout.write(self.style.SUCCESS("Sample data added."))
