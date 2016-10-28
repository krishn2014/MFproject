from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect

# importing models
from models import *

# Create your views here.

# from django.utils import timezone
# from django.contrib.auth.models import User, Group

# Django REST framework
from serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class SchemeDetail(APIView):
    """
    Retrieve details of a schema.
    """
    def get_object(self, schemecode):
        try:
            return Scheme.objects.get(scheme_code=schemecode)
        except Scheme.DoesNotExist:
            raise Http404

    def get(self, request, schemecode, format=None):
        scheme = self.get_object(schemecode)
        serializer = SchemeDetailsSerializer(scheme)
        return Response(serializer.data)

class SearchScheme(APIView):
    """
    Retrieve details of a schema for a given category
    """

    def get(self, request, format=None):
        if 'category' in request.GET:
            schemes  = Scheme.objects.filter(fund=Fund.objects.filter(category__category=request.GET['category']))
            serializer = SchemeSerializer(schemes, many=True)
            return Response(serializer.data)
        return Response("invalid url",status=status.HTTP_404_NOT_FOUND)
