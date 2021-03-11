from rest_framework import serializers

from userSystem.models import User


class MyPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'profile_image', 'profile')
