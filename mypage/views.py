from rest_framework import generics

from mypage.serializers import MyPageSerializer
from userSystem.models import User


class MyPageList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = MyPageSerializer


class MyPageUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = MyPageSerializer
