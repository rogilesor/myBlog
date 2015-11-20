from django.db import models
from blogdef.models import Parution
# Create your models here.
from accounts.models import MyUser

class CommentManager(models.Manager):
	def all(self):
		return super(CommentManager,self).filter(active=True).filter(parent=None).order_by("-timestamp")

	def create_comment(self, user=None, text=None ,path=None, parution=None):
		if not path:
			raise ValueError("Must include a path when adding a comment")
		if not user:
			raise ValueError("Must include a user when adding a comment")
	
		comment = self.model(
			user = user,
			path = path,
			text = text,
			)

		if parution is not None:
			comment.parution = parution
		comment.save(using=self._db)
		return comment


class Comment(models.Model):
	user = models.ForeignKey(MyUser)
	parent = models.ForeignKey("self",null=True,blank=True)
	path = models.CharField(max_length=350)
	parution = models.ForeignKey(Parution,null=True,blank=True)
	text = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	active = models.BooleanField(default=True)

	objects = CommentManager()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		maChaine = self.user.username
		return maChaine

	@property
	def get_comment(self):
		return self.text

	@property
	def is_child(self):
		if self.parent is not None:
			return True
		else :
			return False


	def get_children(self):
		if self.is_child:
			return None
		else :
			return Comment.objects.filter(parent=self)	
	
