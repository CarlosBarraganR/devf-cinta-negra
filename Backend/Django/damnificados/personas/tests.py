# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Personas

from .serializers import PersonasSerializer

import json

# Create your tests here.

class PersonasTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.first_persona = Personas.objects.create(
            name = "Sadot",
            age = 26,
            sex = "M",
            persona_type = "Voluntario")

        self.second_persona = Personas.objects.create(
            name = "Sadot the II",
            age = 26,
            sex = "M",
            persona_type = "Voluntario")

        self.persona_correcta = {
            "name": "Sadot the II",
            "age": 26,
            "sex": "M",
            "persona_type": "Voluntario"
            }

        self.persona_incorrecta = {
            "name": "Sadot the II",
            "age": 26,
            "sex": 666,
            "persona_type": "Voluntario"
        }
    
    def test_get_all_personas(self):
        response = self.client.get(reverse("personas_endpoint"))
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many = True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_get_all_persona(self):
        response = self.client.get(reverse(("persona_endpoint"), kwargs = {'pk': self.first_persona.id}))
        personas = Personas.objects.get(pk= self.first_persona.id)
        serializer = PersonasSerializer(personas)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_post_persona(self):
        response = self.client.post(reverse('personas_endpoint'), 
        data = json.dumps(self.persona_correcta), 
        content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_put_persona(self):
        persona = Personas.objects.get(pk=self.first_persona.id)
        response = self.client.put(reverse('persona_endpoint', kwargs = {'pk': self.second_persona.id}),
        data = json.dumps(self.persona_correcta),
        content_type = 'application/json')
        self.assertEqual(response.status_code, 202)

    def test_delete_persona(self):
        response = self.client.delete(reverse('persona_endpoint', kwargs = {'pk': self.second_persona.id}))
        self.assertEqual(response.status_code, 204)