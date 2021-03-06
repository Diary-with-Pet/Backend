from django.db import models

from userSystem.models import User


class Todo(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="todo", on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=30)
    classification = models.IntegerField(default=1)
