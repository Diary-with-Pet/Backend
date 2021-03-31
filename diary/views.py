from rest_framework import viewsets, permissions

from diary.serializers import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DiarySerializer

    def get_queryset(self):
        return self.request.user.diary_user.all()


# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from diary.models import Diary
# from diary.serializers import DiarySerializer, DiaryListSerializer
#
#
# class DiaryView(APIView):
#
#     permission_classes = (IsAuthenticated, )
#
#     def post(self, request):
#         serializer = DiarySerializer(data=request.data, context={"request": request})
#         if serializer.is_valid():
#             serializer.save(user=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         serializer = DiaryListSerializer(user=self.request.user)
#         return Response(serializer.data)
#
#
# class DiaryDetailView(APIView):
#
#     permission_classes = (IsAuthenticated, )
#
#     def get_object(self, pk):
#         return get_object_or_404(Diary, pk=pk)
#
#     def get(self, request, pk):
#         diary = self.get_object(pk)
#         serializer = DiarySerializer(diary)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
