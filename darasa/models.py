from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from users.models import CustomUser

class Student(models.Model):
	teacher = models.ForeignKey(CustomUser, related_name='students',null=True, blank=True)
	name = models.CharField(blank=False,null=False,default='name' , max_length=128)
	phone = models.CharField(max_length=255)
	modified_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
	    super(Student, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=128)
	number = models.CharField(max_length=128, default='1000')
	students = models.ManyToManyField(Student, through='Registration')

	def save(self, *args, **kwargs):
		if not self.number:
			self.number = timezone.now.date().strftime("%Y%m") + str(int(type(self).Objects.last().number) + 1 ) 
		super(Subject, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name

class Registration(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=64)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name


