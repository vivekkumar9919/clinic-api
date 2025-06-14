from django.urls import path
from .views import DoctorListView, AppointmentListCreateView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctors'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointments'),
]
