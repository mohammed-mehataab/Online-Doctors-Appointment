from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
# from patient.models import Patient
from django import forms
import json
# Create your models here.
dirr = {
    "10AM - 11AM":"10AM - 11AM",
    "11AM - 12PM":'11AM - 12PM',
    "12PM - 1PM":"12PM - 1PM",
    "2PM - 3PM":"2PM - 3PM",
    "3PM - 4PM":"3PM - 4PM"
}

time = json.dumps(dirr)
class Doctors(models.Model):
    choice = (
        ("10AM - 11AM", "10AM - 11AM"),
        ("11AM - 12PM", "11AM TO 12PM"),
        ("12PM - 1PM", "12PM - 1PM"),
        ("2PM - 3PM", "2PM - 3PM"),
        ("3PM - 4PM", "3PM - 4PM")
    )
    spec = (
        ("CARDIO","CARDIO"),
        ("ENT","ENT"),
        ("Anesthesiology","Anesthesiology"),
        ("Dermatology","Dermatology"),
        ("Orthopedic","Orthopedic")
    )
    name = models.CharField(max_length=100, null = True, blank = True)
    specialization = models.CharField(max_length = 100, choices=spec, null= True, blank = True)
    email = models.CharField(max_length=100, null = True, blank = True)
    password = models.CharField(max_length=200, blank = True, null = True)
    price = models.IntegerField(null = True, blank=True, default=100)
    time = models.CharField(max_length=300, default=time)
    profilepic = models.ImageField(null = True, blank = True, default="default.png")

    # profilepic = models.ImageField(null = True, blank = True, default = 'default.png')


class Avail(models.Model):
    # patient = models.ForeignKey(Patient, null = True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null = True, blank = True)
    email = models.CharField(max_length=100, null = True, blank = True)
    pricing = models.CharField(max_length=100, null = True, blank = True)
    specialization = models.CharField(max_length=100 , null = True, blank = True)
    time = models.CharField(max_length=100, null = True, blank = True)
    patientname = models.CharField(max_length=100, null = True, blank = True)
    issue = models.TextField(null = True, blank=True)

class Time(models.Model): 
    choice = (
        ("10AM - 11AM", "10AM - 11AM"),
        ("11AM - 12PM", '11AM TO 12PM'),
        ("12PM - 1PM", "12PM - 1PM"),
        ("2PM - 3PM", "2PM - 3PM"),
        ("3PM - 4PM", "3PM - 4PM")
    )
    id = models.AutoField(primary_key=True)
    timing = models.CharField(max_length=100, choices=choice , null = True, blank=True)

    def __str__(self):
        return str(self.timing)