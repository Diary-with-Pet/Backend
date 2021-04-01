from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todo.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)
