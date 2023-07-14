from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Image(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    message = models.CharField(max_length=200)
    tarih = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.message
