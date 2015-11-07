from django.db import models

# Create your models here.



class Message(models.Model):
	titre = models.CharField(max_length=255)
	auteur = models.CharField(max_length=255)
	mail = models.EmailField()
	sujet = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True,auto_now=False)
	contenu = models.TextField(null=True)


	def __str__(self):
		return self.auteur + " / " + self.titre
