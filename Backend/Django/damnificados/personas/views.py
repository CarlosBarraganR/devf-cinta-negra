# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Personas
from .serializers import PersonasGetNameSerializer, PersonasCreateSerializer, PersonasSerializer

from django.shortcuts import render

import requests

# Create your views here.

class PersonasApi(APIView):

    def get(self, request):
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class PersonaApi(APIView):

    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        persona = self._getPersona(pk)
        persona.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)