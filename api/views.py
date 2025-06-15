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
    serializer_class = DoctorSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        try:
            return Doctor.objects.all().order_by('name')
        except Exception as e:
            print("Error in DoctorListView:", str(e))
            return Doctor.objects.none()  


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
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

    
    # save Appointment in database
    def post(self, request):
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

