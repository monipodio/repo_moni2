
from django.contrib import admin
from django.urls import path, include


# URLS.PY PRINCIPAL DEL PROYECTO

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('polls/', include('polls.urls')),
	path('polls/', include('polls.urls', namespace="polls")),

]
