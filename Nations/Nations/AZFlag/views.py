from django.shortcuts import render
from .models import User, Flag
from django.http import HttpResponse

"""
screen page (main)
"""
# function index
def index(request):
  f = open('media/Nations/files/nations.txt', 'r')
  nations = []
  line = f.readline()
  while line != "":
    flag = Flag(line)
    nations.append(line) 
    line = f.readline()
  f.close()
  if (request.method == "POST"):
    pass
  else:
    return render(request, "AZFlag/index.html", {'data': nations})
