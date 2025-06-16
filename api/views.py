from django.shortcuts import render
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer
from rest_framework import generics , filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .pagination import CustomPageNumberPagination

from api.utils.response_utils import standard_response
class DoctorListView(generics.ListAPIView):
    """
    API view to list all doctors in a paginated format.

    This view returns a list of doctors ordered by their name.
    It uses custom pagination and handles exceptions gracefully.
    """
    serializer_class = DoctorSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        """
        Get the queryset of doctors.

        Returns:
            QuerySet: Ordered list of Doctor objects.
        """
        try:
            return Doctor.objects.all().order_by('name')
        except Exception as e:
            print("Error in DoctorListView:", str(e))
            return Doctor.objects.none()  


class AppointmentListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create appointments.

    Supports:
    - GET method to list appointments (with optional filters like doctor and date).
    - POST method to create a new appointment with validation and formatted response.
    """
    serializer_class = AppointmentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        """
        Get filtered queryset of appointments.

        Filters:
            - doctor (int): Filter appointments by doctor ID.
            - date (YYYY-MM-DD): Filter appointments by date.

        Returns:
            QuerySet: Filtered and ordered Appointment objects.
        """
        try:
            queryset = Appointment.objects.all().order_by('-date', '-time_slot')
            doctor_id = self.request.query_params.get('doctor')
            date = self.request.query_params.get('date')

            if doctor_id:
                queryset = queryset.filter(doctor__id=doctor_id)
            if date:
                queryset = queryset.filter(date=date)

            return queryset
        except Exception as e:
            print("Error in filtering appointments:", str(e))
            return Appointment.objects.none()

    def post(self, request):
        """
        Create a new appointment from the POST request body.

        Request Body Example:
        {
            "patient_name": "Rakesh",
            "doctor": 1,
            "date": "2025-06-15",
            "time_slot": "1:30:00",
            "status": "Scheduled"
        }

        Returns:
            JSON response with status code, message, and data or error.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            print("request body is", serializer)
            if serializer.is_valid():
                instance = serializer.save()
                return standard_response(
                    data=self.get_serializer(instance).data,
                    status_code=201,
                    message="Appointment created successfully"
                )
            return standard_response(
                data=None,
                status_code=400,
                message="Invalid data provided",
                error=serializer.errors
            )
        except Exception as e:
            print("Error while creating appointment:", str(e))
            return standard_response(
                data=None,
                status_code=500,
                message="Something went wrong while creating appointment",
                error=str(e)
            )

