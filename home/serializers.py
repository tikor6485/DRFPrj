from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    newCar = serializers.SlugRelatedField(slug_field='model', read_only = True)
    class Meta:
        model= Person
        fields = ('id', 'newName', 'newAge', 'newEmail', 'newCar')
        extra_kwargs ={
            'newEmail':{'write_only':True}
                      }
    

    def validate_newName(self, value):
        if value == 'admin':
            raise serializers.ValidationError('newName can not be admin')
        return value