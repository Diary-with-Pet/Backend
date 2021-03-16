from rest_framework import viewsets, permissions

from diary.serializers import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DiarySerializer

    def get_queryset(self):
        return self.request.user.diary_user.all()
