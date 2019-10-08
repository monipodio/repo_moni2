from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('',views.login_ini, name="login_ini"),
]
