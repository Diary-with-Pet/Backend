from rest_framework import serializers

from diary.models import DiaryImage, Diary


class DiaryImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = DiaryImage
        fields = ['image']


class DiarySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.diaryimage_set.all()
        return DiaryImageSerializer(instance=image, many=True).data

    class Meta:
        model = Diary
        fields = ['id', 'title', 'content', 'date_created', 'images']

    def create(self, validated_data):
        instance = Diary.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        print(image_set)
        for image_data in image_set.getlist('image'):
            DiaryImage.objects.create(diary=instance, image=image_data)
        return instance
