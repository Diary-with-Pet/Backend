from rest_framework import serializers

from todo.models import Todo
from userSystem.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    todo = UserSerializer(many=True, read_only=False)

    class Meta:
        model = Todo
        fields = ("id", "user_id", "title", "content", "classification")
