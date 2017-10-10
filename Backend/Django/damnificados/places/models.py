# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from personas.models import Personas

# Create your models here.

STATUS = (("1","Actual"),("0","Ya no"))

# Model Places
class Places(models.Model):
    place_name = models.CharField(max_length=45)
    street_name = models.CharField(max_length=45)
    city =  models.CharField(max_length=45)

# Model PersonasHasPlaces 
class PersonasHasPlaces(models.Model):
    date = models.DateField()
    status = models.CharField(choices=STATUS, max_length=20)
    places_id = models.ForeignKey(Places)
    personas_id = models.ForeignKey(Personas)