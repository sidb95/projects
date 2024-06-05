from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf.urls import include # type: ignore
from . import views

app_name = 'AZFlag'

urlpatterns = [
    path('', views.index, name="index"),
    path('AZFlag/index.html', include('AZFlag.urls'))
]
