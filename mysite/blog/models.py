from django.db import models

# Create your models here.

class TimespanModel(models.Model):
	"""docstring for _time"""
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True
			

class Post(TimespanModel):
	title = models.CharField(max_length=255)
	body = models.TextField()


	def __str__(self):
		return self.title