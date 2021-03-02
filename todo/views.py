from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
