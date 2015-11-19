from django.shortcuts import render
from .models import Parution 
from comments.models import Comment
from comments.forms import CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.dates import DayArchiveView
from django.db.models import Q
from django.http import Http404


def publication_list(request):
	articles = Parution.objects.all()
	context = {
		"articles" : articles,
	}
	return render(request,"blogdef/parution_list.html",context)

def publication_detail(request, pk):
	try :
		object = Parution.objects.get(pk=pk)
		comments = Comment.objects.filter(parution=object)
		comment_form = CommentForm(request.POST or None)

		context = {
					"object":object,
					"comments":comments,
				}
		
		if comment_form.is_valid():
			obj_instance = comment_form.save(commit=False)
			obj_instance.path = request.get_full_path()
			obj_instance.user = request.user
			obj_instance.parution = object
			obj_instance.save()
			return render(request,"blogdef/parution_detail.html",context)	

		context["comment_form"]=comment_form
		return render(request,"blogdef/parution_detail.html",context)	
	except :
		raise Http404