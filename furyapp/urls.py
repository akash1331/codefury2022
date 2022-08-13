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
    path('investorsapi/',inverstorsApi.as_view(),name='inverstorsApi'),
    path('feedApi/',feedApi.as_view(),name='feedApi'),
    path('feedApi/<int:pk>/',views.feedindi, name = 'indi'),
    path('investorsapi/<str:pk>/',views.inverstor_indi, name = 'indi'), #use email as pk
    path('tasks/',taskview.as_view(),name='task'),

]
