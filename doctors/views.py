
from django.views.generic import ListView

from django.views.generic import DetailView
from .models import *
from doctors.models import MedicalCard


class PatientSearchForm:
    pass


class DoctorCabinetView(ListView):
    model = Patient
    template_name = 'cabinet.html'


class PatientCardView(DetailView):
    model = MedicalCard
    template_name = 'patient_card.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавляем форму поиска пациентов    
        context['patient_search_form'] = PatientSearchForm()
        return context
    
    