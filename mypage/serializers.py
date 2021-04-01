from rest_framework import serializers

from userSystem.models import User


class MyPageSerializer(serializers.ModelSerializer):

    profile_image = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'profile_image', 'profile')
