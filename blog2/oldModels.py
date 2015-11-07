from django.db import models

class TypeParution(models.Model):
	type_parution = models.CharField(max_length=120)

	def __str__(self):
		return self.type_parution

class Parution(models.Model):
	auteur = models.CharField(max_length=100)
	contenu = models.TextField(default="blabla")
	classement = models.ForeignKey(TypeParution)
	
	def __str__(self):
		return self.auteur

