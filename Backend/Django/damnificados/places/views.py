# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Places
from .serializers import PlacesGetNameSerializer, PlacesCreateSerializer, PlacesSerializer


from django.shortcuts import render

# Create your views here.

class PlacesApi(APIView):

    def get(self, request):
        places = Places.objects.all()
        serializer = PlacesSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlacesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)