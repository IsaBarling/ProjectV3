from django.urls import path

from doctors.views import *

urlpatterns = (
    path('cabinet/', DoctorCabinetView.as_view(), name='cabinet'),
    path('cards/patient-<int:patient_id>/', PatientCardView.as_view(), name='patient_card'),
)
