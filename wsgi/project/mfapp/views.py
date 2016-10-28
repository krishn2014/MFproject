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
