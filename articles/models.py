from django.db import models

# Create your models here.
class article(models.Model):
	Title = models.CharField(max_length=200)
	Author = models.CharField(max_length=200)
	Category = models.CharField(max_length=200)
	Pub_date = models.DateTimeField('date published')
	image_link = models.CharField(max_length=200)
	text_link = models.CharField(max_length=200)
	def __str__(self):
		return self.Title