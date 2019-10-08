from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout

#def index(request):
#	variable1 = 'PAGINA PRINCIPAL'
#	context ={ "variable1":variable1,}
#	return render(request,'index.html',context)


def login_ini(request):
	variable1 = 'Pantalla de Acceso al Sistema'
	error_log = "ok" 
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username, password=password)
	if request.method == "POST":
		if user is not None and user.is_active:
    		# Correct password, and the user is marked "active"
			auth.login(request, user)
			#return HttpResponse("username: "+str(username))
			return HttpResponseRedirect("principal")
		else:
			# Show an error page
			auth.logout(request)
			error_log = "error" 
			context ={
				"variable1":variable1,
				"error_log":error_log,
			}
			return render(request,"login_ini.html",context)
	else:
		auth.logout(request)
		context ={
				'user':user,
				"variable1":variable1,
				"error_log":error_log,
		}
		return render(request,'login_ini.html',context)


def log_out(request):
	logout(request)
	return redirect('login_ini')
