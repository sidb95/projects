from django.db import models # type: ignore


# class Flag
class Flag(models.Model):
  uid = models.IntegerField(default=True)
  countryName = models.CharField(max_length=20)
  imgURL = models.CharField(max_length=100)
  anthemURL = models.CharField(max_length=100, default="")
