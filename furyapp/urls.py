"""furyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('',inverstorsApi.as_view(), name='home'),
    path('investorsapi/',inverstorsApi.as_view(),name='inverstorsApi'), #get and post request of investors data
    path('fund/',fund.as_view(),name='fund'),  #to show total fund of an individual startup
    path('fund/<int:pk>',fund.as_view(),name='fund'),  #to put and get total fund of an individual startup
    path('invest/',invest.as_view(),name='invest'),  #to show total fund of an individual startup
    path('invest/<int:pk>',invest.as_view(),name='invest'),  #to put and get total fund of an individual startup
    path('startupdata/<int:pk>',startupdata.as_view(),name='startupdata'), #startup data complete
    path('feedApi/',feedApi.as_view(),name='feedApi'), #startup posts get post delete
    path('feedApi/<int:pk>/',views.feedindi, name = 'indi'), #startup post put
    path('investorsapi/<str:pk>/',views.inverstor_indi, name = 'indi'), #use email as pk    #get investors data
    path('tasks/',taskview.as_view(),name='task'), #task given by a company

]
