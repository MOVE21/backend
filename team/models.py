from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.TextField()
    players = models.ManyToManyField(User, related_name="team_player")
    cap = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_captian", null=True)
    code = models.TextField(null=True)
