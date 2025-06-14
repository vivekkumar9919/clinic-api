from django.shortcuts import render
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer
from rest_framework import generics , filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .pagination import CustomPageNumberPagination


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
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # saves to DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
