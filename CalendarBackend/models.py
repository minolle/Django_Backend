from django.db import models
#from rest_framework import serializers
# Create your models here.

class Appointment(models.Model):
  created = models.DateField(auto_now_add=True)
  date = models.DateTimeField()
  time_provided = models.BooleanField()
  text = models.CharField(max_length=200)
  title = models.CharField(max_length=25)
  owner = models.ForeignKey('auth.User', related_name='appointments', on_delete=models.CASCADE)

  class Meta:
    ordering = ['date', 'title', 'created']
  


class NoteLine(models.Model):
  line_idx = models.IntegerField(unique=True)
  line_text = models.CharField(max_length=42)
  
  class Meta:
    ordering = ['line_idx']
  
