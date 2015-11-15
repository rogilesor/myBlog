from django.shortcuts import render
from django.conf import settings
from blog2.models import Parution
#from blog.models import Article
# Create your views here.

def home(request):
	maConnexions = settings.DATABASES['default']['ENGINE']
	maBaseDonnees = settings.DATABASES['default']['NAME']
	#print(maConnexions)
	template = 'testeur/testeur.html'
	context = {'fichier_base':settings.BASE_DIR,
				'db':maConnexions,
				'nomdb': maBaseDonnees,
				'user':request.user,
				'authentifie':request.user.is_authenticated}
	return render(request,template,context)



from accounts.forms import RegisterForm
from accounts.models import MyUser
from django.utils.safestring import mark_safe

def srvup(request):
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']

		MyUser.objects.create_user(username=username,email=email,password=password)
		print(username,email,password)

	# name = "igor"
	# parutions = Parution.objects.all()
	# embeds = []

	# for parution in parutions:
	# 	texte = mark_safe(parution.contenu)
	# 	embeds.append(texte)

	context = {
		"action_value":"",
		"submit_btn_value":"Register",
		# "the_name":name,
		# "number":parutions.count(),
		# "parutions":parutions,
		# "the_embeds":embeds,
		# "a_code":mark_safe(parutions[0].contenu),
		"form":form
	}
	return render(request,'form.html',context)