from rest_framework import generics, permissions

from mypage.serializers import MyPageSerializer
from userSystem.models import User


class MyPageList(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MyPageSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class MyPageUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MyPageSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
