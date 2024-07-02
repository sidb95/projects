from django.shortcuts import render
from .models import Flag
from django.http import HttpResponse
from Authenticator.models import Person

"""
screen page (main)
"""
# function index
def index(request):
  nations = {}
  urls = []
  if (len(Flag.objects.all()) < 1):
    f = open('AZFlag/static/AZFlag/files/nations_sorted.txt', 'r')
    line = f.readline()
    count = 0
    while line != "":
      count += 1
      nation = ""
      code = ""
      try:
        arr = line.split(' ')
        nation = arr[0]
        code = arr[1]
      except IndexError as err:
        print("list Index Out of range", err)
      flag = Flag(countryName=nation, imgURL=(code + ".png"), anthemURL="")
      flag.save() 
      nations[flag.countryName] = flag.imgURL
      urls.append(code + '.png')
      line = f.readline()
    f.close()
    f = open('AZFlag/static/AZFlag/files/national_anthems.txt')
    line = f.readline()
    while (line != ""):
        try:
            arr = line.split()
            nation = arr[0]
            anthemURL = arr[2]
            flag = Flag.objects.get(countryName=nation)
            flag.anthemURL = anthemURL
            flag.save()
            line = f.readline()
        except IndexError as err:
            print("list Index Out of range", err)
  else:
    flags = Flag.objects.all()
    for flag in flags:
      nations[flag.countryName] = {flag.imgURL: flag.anthemURL}
  if (request.method == "POST"):
    pass
  else:
    return render(request, "AZFlag/index.html", {'nations': nations})
