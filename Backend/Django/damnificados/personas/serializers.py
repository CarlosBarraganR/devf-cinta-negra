from rest_framework import serializers
from .models import Personas

SEXOS = (("M","Mujer"),("H","Hombre"),("I","Indefinido"))
TIPOPERSONA = (("Voluntario","Voluntario"),("Damnificado","Damnificado"),("Otro","Otro"))

def validar_dato(source):
    if source <= 100:
        pass
    else:
        raise serializers.ValidationError("No hay edad mayor a 100")

class PersonasCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    edad = serializers.IntegerField(validators= [validar_dato])
    sexo = serializers.CharField(max_length=100)
    tipo_de_persona = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return Personas.objects.create(**validated_data)

class PersonasGetNameSerializer(serializers.Serializer):
    name = serializers.CharField()

class PersonasModifySerializer(serializers.Serializer):
    tipo_de_persona = serializers.CharField()
