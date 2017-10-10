from rest_framework import serializers
from .models import Places

# PLACES MODEL SERIALIZERS

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ['place_name', 'street_name', 'city']

class PlacesCreateSerializer(serializers.Serializer):
    place_name = serializers.CharField(max_length=45)
    street_name = serializers.CharField(max_length=45)
    city = serializers.CharField(max_length=45)
    def create(self, validate_data):
        return Places.objects.create(**validate_data)

class PlacesGetNameSerializer(serializers.Serializer):
    place_name = serializers.CharField()
    street_name = serializers.CharField()
    city = serializers.CharField()