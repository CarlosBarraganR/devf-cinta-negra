# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Places

from .serializers import PlacesSerializer

import json

# Create your tests here.

class PlacesTest(TestCase):
    def setUp():
        self.client = Client()

        self.first_place = Places.objects.create(
            place_name = "Plazita Linda"
            street_name = "Lindavista #4434"
            city = "Zapopan"
        )

        def test_get_places(self):
            places = Places.objects.all()
            response = 
