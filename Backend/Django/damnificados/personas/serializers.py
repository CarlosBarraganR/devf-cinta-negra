from rest_framework import serializers
from .models import Personas

def validate_data(source):
    if source <= 100:
        pass
    else:
        raise serializers.ValidationError("No hay edad mayor a 100")

# PERSONAS MODEL SERIALIZERS
class PersonasCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(validators= [validate_data])
    sex = serializers.CharField(max_length=100)
    persona_type = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return Personas.objects.create(**validated_data)

class PersonasGetNameSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    sex = serializers.CharField()
    persona_type = serializers.CharField()

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['id','name', 'age','sex','persona_type']

class PersonasModifySerializer(serializers.Serializer):
    tipo_de_persona = serializers.CharField()