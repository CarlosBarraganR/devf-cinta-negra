# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Model Personas
class Personas(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex =  models.CharField(max_length=100)
    persona_type = models.CharField(max_length=100)