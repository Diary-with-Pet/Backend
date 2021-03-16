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

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        diary = Diary.objects.create(**validated_data)
        for image_data in images_data.getlist('image'):
            DiaryImage.objects.create(diary=diary, image=image_data)
        return diary

