from django.urls import path, re_path, register_converter
from django.views.generic import DetailView

from doctors.views import DoctorCabinetView, PatientCardView
from . import views
from .views import HomeView

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('cabinet/', DoctorCabinetView.as_view(), name='cabinet'),
    path('patients/<int:patient_id>/', PatientCardView.as_view(), name='patient_card'),
]

