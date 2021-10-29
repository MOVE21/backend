from django.db import models
from django.contrib.auth.models import User
from matches.models import Match
from team.models import Team


class Position(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()


class Stadion(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    players = models.ManyToManyField(User, null=True)
    matches = models.ManyToManyField(Match, null=True)
    teams = models.ManyToManyField(Team, null=True)
