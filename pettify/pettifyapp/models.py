from django.db import models

import datetime
from django.utils import timezone


# Create your models here.
class Animal(models.Model):
	male = 'Male'
	female = 'Female'
	none = ''
	gender_choices = (
		('none', none),
		('male', male),
		('female', female),
	)
	image = models.FileField(null=True, blank=True)
	category = models.CharField(max_length=60)
	name = models.CharField(max_length=60)
	shelter = models.CharField(max_length=60)
	age = models.IntegerField(default=0)
	gender = models.CharField(default=none, choices=gender_choices, max_length=6)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.category

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

