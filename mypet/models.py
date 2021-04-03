from django.db import models

from userSystem.models import User


class MyPet(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='사용자', related_name="mypet", on_delete=models.CASCADE, null=True)
    pet_name = models.CharField(verbose_name='펫 이름', max_length=20)
    birthday = models.CharField(verbose_name='생일', max_length=15)
    gender = models.IntegerField(verbose_name='성별', default=2)
    species = models.CharField(verbose_name='종', max_length=20)
    profile_image = models.ImageField(verbose_name='프로필 이미지', default='media/pet/default_image.jpeg', upload_to='pet',
                                      blank=True, null=True)
    profile = models.CharField(verbose_name='프로필 내용', max_length=80, blank=True)

    def __str__(self):
        return f"{self.user}/{self.pet_name}"

    class Meta:
        verbose_name = '펫'
        verbose_name_plural = verbose_name
