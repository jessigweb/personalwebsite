from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


class codeschool(models.Model):
	course = models.CharField(max_length=30)
	badge = models.CharField(max_length=100)
	#add public url for course
	
	def __str__(self):
	       return self.course
	def was_published_recently(self):
	    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class codeacademy(models.Model):
	language = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	
	def __str__(self):
	       return self.language
	def was_published_recently(self):
	    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=30)
	budget = models.CharField(max_length=30)
	start = models.CharField(max_length=30)
	project = models.CharField(max_length=1000)

	def __str__(self):
	    return self.name
	def was_published_recently(self):
	    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
