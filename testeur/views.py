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



