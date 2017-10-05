# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Personas
from .serializers import PersonasGetNameSerializer, PersonasCreateSerializer

from django.shortcuts import render

# Create your views here.

class PersonasApi(APIView):

    def get(self, request):
        personas = Personas.objects.all()
        serializer = PersonasGetNameSerializer(personas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonasCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)