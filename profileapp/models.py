from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    midname = models.TextField(null=True)
    photo = models.ImageField(null=True)
    descr = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)