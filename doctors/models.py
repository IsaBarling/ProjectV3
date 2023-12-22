from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.last_name


class MedicalCard(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    recommendations = models.TextField()

    def __str__(self):
        return self.id
