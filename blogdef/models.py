from django.db import models
from datetime import datetime  


class TypeParution(models.Model):
	type_parution = models.CharField(max_length=120)

	def __str__(self):
		return self.type_parution

class Parution(models.Model):
	titre = models.CharField(max_length=255,default="sans titre")
	auteur = models.CharField(max_length=100)
	contenu = models.TextField(default="blabla")
	# slug = models.SlugField(unique=True,null=True,blank=True)
	classement = models.ForeignKey(TypeParution)
	date = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Date de parution")

	def __str__(self):
		return self.titre

