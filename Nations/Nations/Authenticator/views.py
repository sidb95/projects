from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Person
import random
from django.http import HttpResponseRedirect
from django.urls import reverse, path
import AZFlag

class Authenticator():

  def __init__(self, usrA):
    self.act = usrA.act

  # function ```getACT```
  def getACT(self):
    return self.act

  # function ```check_act```
  def checkACT(self, act):
    for user in Person.objects.all():
      if (act == user.act):
        return True
    return False


def get_params(request, key):
  act = "tokenA1"
  if(request.GET.get(key) != None):
    act = request.GET.get(key)
  return {'act': act}


def calcToken():
  chars = ['A', 'B', 'C']
  answer = "token" + chars[random.randint(0, 2)]
  answer += str(random.randint(1, 100))
  return answer


def index(request):
  if request.method == "GET":
    id = 1
    if (Person.objects is not None):
      id = len(Person.objects.all()) + 1
    token = calcToken()
    usrInstance = Person.objects.create(sid=id, act=token)
    usrInstance.save()
    auth = Authenticator(usrInstance)
    params = get_params(request, 'act')
    if (auth.checkACT((params['act']))):
      return redirect('AZFlag:index')
    else:
      print(token)
      return render(request, ('Authenticator/index.html'), context=params)
