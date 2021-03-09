from rest_framework import serializers

from mypet.models import MyPet


class MyPetSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyPet
        fields = ('id', 'pet_name', 'gender', 'species', 'species_detail', 'profile')
