from rest_framework import serializers
from .models import Doctor , Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.StringRelatedField(source='doctor', read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'        