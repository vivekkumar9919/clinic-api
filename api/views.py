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
    queryset = Doctor.objects.all().order_by('name')  # or any order you prefer
    serializer_class = DoctorSerializer
    pagination_class = CustomPageNumberPagination

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Appointment.objects.all().order_by('-date', '-time_slot')
        print(str(queryset.query))
        doctor_id = self.request.query_params.get('doctor')
        date = self.request.query_params.get('date')

        if doctor_id:
            queryset = queryset.filter(doctor__id=doctor_id)
        if date:
            queryset = queryset.filter(date=date)

        return queryset
    
    # save Appointment in database
    def post(self, request):
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
