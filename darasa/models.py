from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
	owner = models.ForeignKey('auth.User', related_name='students',null=True, blank=True)
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
		self.number = str(int(self.number) + 1 ) 
		super(Subject, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name

class Registration(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=64)