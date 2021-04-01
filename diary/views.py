from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from diary.serializers import DiarySerializer, DiaryListSerializer


class DiaryViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DiarySerializer

    def get_queryset(self):
        return self.request.user.diary_user.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.request.user.diary_user.all()
        serializer = DiaryListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
