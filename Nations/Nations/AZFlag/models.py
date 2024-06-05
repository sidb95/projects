from django.db import models # type: ignore


# class Flag
class Flag(models.Model):
  countryName = models.CharField(max_length=20)
  imgURL = models.CharField(max_length=100)
