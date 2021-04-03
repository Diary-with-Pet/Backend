from rest_framework import serializers

from mypet.models import MyPet


class MyPetSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = MyPet
        fields = ('id', 'pet_name', 'gender', 'birthday', 'species', 'profile_image', 'profile')
