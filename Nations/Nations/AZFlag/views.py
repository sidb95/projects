from django.shortcuts import render # type: ignore
from .models import User

"""
screen page (main)
"""
# function index
def index(request):
  if (request.method == "POST"):
    pass
  else:
    return render(request, "index.html")
