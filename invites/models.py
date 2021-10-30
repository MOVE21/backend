from django.db import models
from django.contrib.auth.models import User
from team.models import Team


class Status(models.Model):
    name = models.TextField()


class UserInvite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_invite = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    descr = models.TextField(null=True)


class TeamInvite(models.Model):
    inviting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="my_invites", null=True)
    team_to_invite = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="inviting_teams", null=True)
    descr = models.TextField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
