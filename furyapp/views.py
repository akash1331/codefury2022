from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework import serializers
from .models import  *
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import  render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import  api_view, permission_classes,authentication_classes
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from django_filters.rest_framework  import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

  

class inverstorsApi(APIView):               #investors list get and post request
    def get(self,request):
        object = investors.objects.all()
        serializer = inverstorsSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = inverstorsSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class feedApi(APIView):               #startup_data get and post request
    def get(self,request):
        object = startup_post.objects.all()
        serializer = startup_postSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = startup_postSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




def feedindi(request,pk):
    try:
        a = startup_post.objects.get(pk = pk)
    except startup_post.DoesNotExist:
        return HTTPResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = startup_postSerializer(a)
        return JsonResponse(serializer.data)


def inverstor_indi(request,pk):
    try:
        a = investors.objects.get(pk = pk)
    except investors.DoesNotExist:
        return HTTPResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = inverstorsSerializer(a)
        return JsonResponse(serializer.data)