from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from diary.models import Diary
from diary.serializers import DiarySerializer


class DiaryPostView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = DiarySerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = self.request.user
        diary = Diary.objects.filter(user_id=user.id)
        serializer = DiarySerializer(diary, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
