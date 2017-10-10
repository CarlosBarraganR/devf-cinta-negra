# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Model Places
class Places(models.Model):
    place_name = models.CharField(max_length=45)
    street_name = models.CharField(max_length=45)
    city =  models.CharField(max_length=45)