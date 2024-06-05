from django.db import models


# class User
class Person(models.Model):
  sid = models.IntegerField()
  act = models.CharField(max_length=9)