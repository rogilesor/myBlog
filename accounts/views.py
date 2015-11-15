from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from accounts.models import MyUser
from django.utils.safestring import mark_safe
from accounts.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.urlresolvers import reverse


def mylogin(request):
	form = LoginForm(request.POST or None)
	
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		
		try :
			the_user = MyUser.objects.get(username=username)
			user = authenticate(username=the_user.username,password=password)
		except :
			user = None

		if user is not None:

			# user = authenticate(username=the_user.username,password=password)

			if user.is_active:
				login(request,user)
				messages.success(request, 'Vous êtes maintenant connecté')	

			else:
				messages.success(request, "Votre compte est en attente d'activation")
				pass
		else:
			return redirect('/register/')

	context = {'form':form}
	return render(request,"registration/login.html",context)

def mylogout(request):
	logout(request)
	return redirect('/login/')

def register(request):

	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		#MyUser.objects.create_user(username=username, email=email, password=password)
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.is_active = False
		messages.success(request, "Enregistrement terminé. Votre compte est maintenant en attente d'activation")
		#new_user.password = password #WRONG
		new_user.set_password(password) #RIGHT
		new_user.save()

	action_url = reverse("register")
	title = "Register"
	submit_btn = "Create free account"

	context = {
		"form": form,
		"action_url": action_url,
		"title": title,
		"submit_btn": submit_btn
		}
	return render(request, "registration/registration_form.html", context)

