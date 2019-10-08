from django.contrib import admin

# Register your models here.

from .models import Param

#class PacientesAdmin(admin.ModelAdmin):
#    fields = ('rut', 'nombre')

admin.site.register(Param)

