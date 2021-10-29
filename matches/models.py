from django.db import models
from team.models import Team


class Participing(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)


class Match(models.Model):
    participings = models.ManyToManyField(Participing)
    is_complete = models.BooleanField(default=False)
    time_holding = models.DateTimeField()
