from django.shortcuts import render
from .models import Flag
from django.http import HttpResponse

"""
screen page (main)
"""
# function index
def index(request):
  f = open('media/Nations/files/nations.txt', 'r')
  nations = []
  line = f.readline()
  count = 0
  while line != "":
    count += 1
    flag = Flag(countryName=line, imgURL=("imgURL" + str(count) + ".png"))
    flag.save() 
    nations.append(line)
    line = f.readline()
  f.close()
  if (request.method == "POST"):
    pass
  else:
    return render(request, "AZFlag/index.html", {'data': nations})
