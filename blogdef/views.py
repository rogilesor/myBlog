from django.shortcuts import render, HttpResponseRedirect
from .models import Parution 
from comments.models import Comment
from comments.forms import CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.dates import DayArchiveView
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def publication_list(request):
	mesArticles = Parution.objects.all()
	paginator = Paginator(mesArticles,2)
	page = request.GET.get('page')
	print(paginator.num_pages)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger :
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
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
			comment_text = comment_form.cleaned_data['comment']
			print(comment_text)
			print(request.user)
			print(object)
			print(request.get_full_path())
			print(object.get_absolute_url())
			new_comment = Comment.objects.create_comment(user=request.user,text=comment_text,path=request.get_full_path(),parution=object)
			return HttpResponseRedirect(object.get_absolute_url())
			return render(request,"blogdef/parution_detail.html",context)	

		context["comment_form"]=comment_form
		return render(request,"blogdef/parution_detail.html",context)	
	except :
		raise Http404