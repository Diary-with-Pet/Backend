from rest_framework import serializers

from userSystem.models import User


class MyPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'profile_image')
