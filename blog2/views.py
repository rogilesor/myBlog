from django.shortcuts import render
from .models import Parution 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.dates import DayArchiveView
from django.db.models import Q


class ParutionDetailView(DetailView):
	model = Parution



class ParutionListView(ListView):
	model = Parution
	queryset = Parution.objects.all().order_by('-date')
	paginate_by = 2


	def get_context_data(self,*args,**kwargs):
		context = super(ParutionListView,self).get_context_data(*args,**kwargs)
		context['nbrParutions'] = len(Parution.objects.all())
		context["query"] = self.request.GET.get("q")
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super(ParutionListView,self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
				Q(contenu__icontains=query) |
				Q(titre__icontains=query) 
				)
		return qs

# titre = mod
# auteur = mo
# contenu = m
# classement 
# date = mode

