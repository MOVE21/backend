from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class Avatar(models.Model):
    image = models.ImageField(null=True)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)


class Profile(models.Model):
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    midname = models.TextField(null=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True)
    descr = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=User)
def token_generate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)
