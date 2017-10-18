# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Places
from .serializers import PlacesSerializer

from django.shortcuts import render
import requests
import json

# Create your views here.

class PlacesApi(APIView):

    def get(self, request):
        places = Places.objects.all()
        serializer = PlacesSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlacesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceApi(APIView):

    def _getPlace(self, pk):
        try:
            return Places.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise HTTP_400_BAD_REQUEST

    def get(self, request, pk):
        place = self._getPlace(pk)
        serializer = PlacesSerializer(place)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        place = self._getPlace(pk)
        serializer = PlacesSerializer(place, request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        place = self._getPlace(pk)
        place.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# class PersonaHasLugaresApi(APIView):

#     def get(self, request):
#         personaHasPlaces = PersonaHasPlaces.objects.all()
#         serializer = PersonaHasPlacesSerializer(personaHasPlaces, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PersonaHasPlacesSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)