from django.db import models


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey("userSystem.User", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=30)
    classification = models.IntegerField
