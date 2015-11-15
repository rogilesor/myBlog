from django.shortcuts import render, redirect

from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

def mylogin(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		print('Attention')
		
		try :
			the_user = User.objects.get(username=username)
		except :
			the_user = None


		print(the_user)

		if the_user is not None:
			user = authenticate(username=the_user.username,password=password)
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

def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		new_user, created = User.objects.get_or_create(username=username,email=email)
		if created:
			new_user.password = password
			new_user.is_active = False
			new_user.save()
			messages.success(request, "Enregistrement terminé. Votre compte est maintenant en attente d'activation")
	context = {'form':form}
	return render(request,"registration/registration_form.html",context)

def mylogout(request):
	logout(request)
	return redirect('/login/')
