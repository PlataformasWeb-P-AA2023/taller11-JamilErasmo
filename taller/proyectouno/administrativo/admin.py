from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Edificio, Departamento

admin.site.register(Edificio)
admin.site.register(Departamento)