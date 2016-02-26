from django.db import models

import datetime
from django.utils import timezone


# Create your models here.
class Selector(models.Model):
	category = models.CharField(max_length=60)	
	def __unicode__(self):
		return self.category
	def __str__(self):
		return self.category

class House(models.Model):
	home = models.CharField(max_length=60)	
	phone = models.CharField(max_length=60)	
	def __unicode__(self):
		return self.home
	def __str__(self):
		return self.home

		

class Animal(models.Model):
	animal_name = models.CharField(max_length=60)
	Male = 'Male'
	Female = 'Female'
	none = ''
	gender_choices = (
		('none', none),
		('Male', Male),
		('Female', Female),
	)
	image = models.FileField(null=True, blank=True)
	category = models.ForeignKey('Selector', on_delete=models.CASCADE)
	shelter = models.ForeignKey('House', on_delete=models.CASCADE)
	age = models.IntegerField(default=0)
	gender = models.CharField(default=none, choices=gender_choices, max_length=6)
	updated = models.DateTimeField(auto_now=False,auto_now_add=True)
	timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
	
	
	def __unicode__(self):
		return self.animal_name
	def __str__(self):
		return self.animal_name

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

