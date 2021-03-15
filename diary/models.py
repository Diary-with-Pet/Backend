from django.db import models

from userSystem.models import User


class Diary(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="diary", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=800)
    date_created = models.DateField(auto_now_add=True)

    image1 = models.ImageField(default='media/diary/default_image.jpeg', upload_to='diary',
                               blank=True, null=True)
    image2 = models.ImageField(default='media/diary/default_image.jpeg', upload_to='diary',
                               blank=True, null=True)
    image3 = models.ImageField(default='media/diary/default_image.jpeg', upload_to='diary',
                               blank=True, null=True)
    image4 = models.ImageField(default='media/diary/default_image.jpeg', upload_to='diary',
                               blank=True, null=True)
