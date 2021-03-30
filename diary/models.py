from django.db import models

from userSystem.models import User


class Diary(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="diary_user", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=800)
    date_created = models.DateField(auto_now_add=True)


class DiaryImage(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    image = models.ImageField(default='/media/diary/default_image.jpeg', upload_to='diary',
                              blank=True, null=True)
