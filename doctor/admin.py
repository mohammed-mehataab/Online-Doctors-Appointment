from pydoc import Doc
from django.contrib import admin
from . models import Doctors, Time, Avail
# Register your models here.

admin.site.register(Doctors)
admin.site.register(Time)
admin.site.register(Avail)
