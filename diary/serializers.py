from rest_framework import serializers

from diary.models import DiaryImage, Diary


class DiaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryImage
        fields = 'image'


class DiarySerializer(serializers.ModelSerializer):
    images = DiaryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ('id', 'title', 'content', 'date_created', 'images')
