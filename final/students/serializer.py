from rest_framework import serializers
from.models import Student

class Studentserilizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','Username','Password')
