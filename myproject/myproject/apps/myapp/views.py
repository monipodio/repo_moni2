from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	variable1 = 'Página diseñada por Gabriel Araya Garcia'
	return render(request,'../templates/post_list2.html',{'variable1': variable1})

	#return HttpResponse("Hola prueba de despliegue de texto directo desde la vista,..")