from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import MessageForm
from django.core.mail import send_mail
from smtplib import SMTP
from django.contrib import messages

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.template import Context
from django.template.loader import render_to_string

# from django.conf import SETTINGS

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

		frm = 'istarosel@1star.link'
		to = ['istarosel@gmail.com']

		c = Context({'titre':titre,'auteur':auteur,'sujet':sujet,'email':email,'contenu':contenu})
		html_content = render_to_string('message/email_inform.html', c)
		monMsg = html_content

		s = SMTP()
		s.connect('smtp.webfaction.com')
		s.login('istarosel','igor1975staroseltsev')

		
		msg = MIMEMultipart('alternative')
		msg.set_charset('utf8')
		msg['Subject'] = "un nouveau message sur 1star.link"
		_attach = MIMEText(monMsg.encode('utf-8'), 'html', 'UTF-8')        

		msg.attach(_attach)
		s.sendmail(frm, to, msg.as_string())
		s.quit()

		messages.success(request, 'Votre mail envoye')		

	return render(request,template,context)

