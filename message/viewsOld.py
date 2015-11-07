from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import MessageForm
from django.core.mail import send_mail
from smtplib import SMTP
from django.contrib import messages

# from django.conf import SETTINGS
#Attention : cela ne supporte que les ascii !!

def myMessage(request):
	form = MessageForm(request.POST or None)
	context = {'form':form}
	template = 'message/monMessage.html'


	if form.is_valid():
		# print(form.cleaned_data)
		titre = form.cleaned_data['titre']
		auteur = form.cleaned_data['auteur']
		contenu = form.cleaned_data['contenu']
		sujet = form.cleaned_data['sujet']
		email = form.cleaned_data['mail']
		form.save()
		from_addr = 'istarosel@1star.link'
		to_addrs = ['istarosel@gmail.com']

		msg = "Vous avez recu un nouveau message : \n" + "auteur : " + auteur + "\n" + "titre : " \
						+ titre + "\n" + "sujet : " + sujet + "\n" + "contenu : " + contenu + "\n" 
		msg.encode('utf-8')
		s = SMTP()
		s.connect('smtp.webfaction.com')
		s.login('istarosel','igor1975staroseltsev')
		s.sendmail(from_addr, to_addrs, msg)
		messages.success(request, 'Votre mail a été envoyé')		
	return render(request,template,context)

