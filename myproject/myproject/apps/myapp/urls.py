
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
]

# para ejecutar el proyecto: http://127.0.0.1:8000/myapp/