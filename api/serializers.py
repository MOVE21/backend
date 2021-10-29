from rest_framework.serializers import Serializer, ModelSerializer
from stadion.models import Stadion, Position
from matches.models import Match, Participing
from team.models import Team
from profileapp.models import Profile
from django.contrib.auth.models import User
from .mixins import stadion_change, match_change, participing_change, team_change


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = ("longitude", "latitude")


class StadionSerializer(ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Stadion
        fields = ("position", "players", "matches", "teams", "id")
        extra_kwargs = {
            "players": {
                "allow_empty": True
            },
            "matches": {
                "allow_empty": True
            },
            "teams": {
                "allow_empty": True
            }
        }

    def create(self, data):
        print(data)
        pos = Position.objects.create(**data["position"])
        stadion = Stadion.objects.create(position=pos)
        stadion = stadion_change(stadion, data)
        return stadion

    def update(self, instance, validated_data):
        return stadion_change(instance, validated_data)


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ("name", "players", "cap", "code")

        extra_kwargs = {
            "players": {
                "allow_empty": True,
            },
            "code": {
                "required": False
            }
        }

    def create(self, validated_data):
        team = Team.objects.create(
            code=validated_data["code"],
            cap=validated_data["cap"],
            name=validated_data["name"])
        team = team_change(team, validated_data)
        return team

    def update(self, instance, validated_data):
        return team_change(instance, validated_data)


class ParticipingSerializer(ModelSerializer):
    class Meta:
        model = Participing
        fields = ("team", "score")
        extra_kwargs = {
            "score": {
                "required": False,
            }
        }

    def create(self, data):
        score = None
        try:
            score = data["score"]
        except KeyError:
            pass
        return Participing.objects.create(score=score, team=data["team"])

    def update(self, instance, validated_data):
        participing_change(instance, validated_data)


class MatchSerializer(ModelSerializer):

    class Meta:
        model = Match
        fields = ("participings", "is_complete", "time_holding")

        extra_kwargs = {
            "participings": {
                "allow_empty": True
            },
            "is_complete": {
                "required": True
            }
        }

    def create(self, validated_data):
        match = Match.objects.create(
            time_holding=validated_data["time_holding"],
            is_complete=validated_data["is_complete"],
        )
        match = match_change(match, validated_data)
        return match

    def update(self, instance, validated_data):
        return match_change(instance, validated_data)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("name", "surname", "midname", "photo", "user")
        extra_kwargs = {
            "name": {
                "required": False,
                "allow_blank": True,
            },
            "surname": {
                "required": False,
                "allow_blank": True,
            },
            "midname": {
                "required": False,
                "allow_blank": True,
            },
            "photo": {
                "required": False,
                "allow_blank": True,
            }
        }

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
