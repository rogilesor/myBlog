from django.db import models
from blog2.models import Parution
# Create your models here.
from accounts.models import MyUser

class CommentManager(models.Manager):
	def create_comment(self, user=None, comment=None ,path=None, parution=None):
		if not path:
			raise ValueError("Must include a path when adding a comment")
		if not user:
			raise ValueError("Must include a user when adding a comment")
	
		comment = self.model(
			user = user,
			path = path,
			comment = comment
			)

		if parution is not None:
			comment.parution = parution
		comment.save(using=self._db)
		return comment


class Comment(models.Model):
	user = models.ForeignKey(MyUser)
	path = models.CharField(max_length=350)
	parution = models.ForeignKey(Parution,null=True,blank=True)
	text = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	active = models.BooleanField(default=True)

	objects = CommentManager()

	def __str__(self):
		return self.user.username
