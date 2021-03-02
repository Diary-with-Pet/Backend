from django.db import models

from userSystem.models import User


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=30)
    classification = models.IntegerField
