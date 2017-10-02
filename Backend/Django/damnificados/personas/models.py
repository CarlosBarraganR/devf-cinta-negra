# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEXOS = (("M","Mujer"),("H","Hombre"),("I","Indefinido"))
TIPOPERSONA = (("Voluntario","Voluntario"),("Damnificado","Damnificado"),("Otro","Otro"))

# Model Personas
class Personas(models.Model):
    name = models.CharField(max_length = 100)
    edad = models.IntegerField(max_length = 3)
    sexo =  models.CharField(choices = SEXOS, max_length = 5)
    tipo_de_persona = models.CharField(choices = TIPOPERSONA, max_length = 50)