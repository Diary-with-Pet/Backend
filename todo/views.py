from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo
from todo.serializers import TodoSerializer


@permission_classes([IsAuthenticated])
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
