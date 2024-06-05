from django.db import models
from rest_framework.authtoken.models import Token


# class User
class User(models.Model):
  sid = models.CharField(max_length=10)
  act = Token.objects.create(user=sid).key

