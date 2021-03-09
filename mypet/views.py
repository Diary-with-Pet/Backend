from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from mypet.models import MyPet
from mypet.serializers import MyPetSerializer


class MyPetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MyPetSerializer

    def get_queryset(self):
        return self.request.user.mypet.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)
