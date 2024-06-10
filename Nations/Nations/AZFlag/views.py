from django.shortcuts import render
from .models import Flag
from django.http import HttpResponse
from Authenticator.models import Person

"""
screen page (main)
"""
# function index
def index(request):
  nations = []
  if (len(Flag.objects.all()) < 1):
    f = open('media/Nations/files/nations.txt', 'r')
    line = f.readline()
    count = 0
    while line != "":
      count += 1
      flag = Flag(countryName=line, imgURL=("imgURL" + str(count) + ".png"))
      flag.save() 
      nations.append(line)
      line = f.readline()
    f.close()
  else:
    flags = Flag.objects.all()
    for flag in flags:
      nations.append(flag.countryName)
  if (request.method == "POST"):
    pass
  else:
    return render(request, "AZFlag/index.html", {'data': nations})
