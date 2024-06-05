from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import User
from .forms import AccessForm


class AccessToken():
# function ```check_act```
  def __init__(self, user):
    self.user = user

  def getACT(self):
    return self.user.act

  def check_act(self, act):
    return (act == self.getACT())


def get_params(request, key):
  return {'act': request.GET.key(key)}

# Number of users that visited
noUsers = 0


def index(request):
  if request.method == "GET":
    noUsers += 1
    params = get_params(request, 'act')
    user = User(noUsers)
    actInstance = AccessToken(user)
    try:
      if (actInstance.check_act(params['act'])):
        redirect(request, "AZFlag/index.html")
    except:
      pass
    finally:
      render(request, "Authenicate/index.html")
