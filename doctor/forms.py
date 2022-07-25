from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
# from dataclasses import field
# from django.forms import ModelForm 
from . models import Doctors, Avail

class DoctorForm(serializers.ModelSerializer): 
    class Meta: 
        model = Doctors
        fields = "__all__"

class AvailForm(serializers.ModelSerializer):
    class Meta:
        model = Avail
        fields = "__all__"