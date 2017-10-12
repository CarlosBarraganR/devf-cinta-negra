from rest_framework import serializers
from .models import Places

# PLACES MODEL SERIALIZERS

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ['place_name', 'street_name', 'city']

# class PersonaHasPlacesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonaHasPlaces
#         fields = ['date', 'status', 'places_id', 'personas_id']