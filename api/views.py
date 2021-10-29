from django.shortcuts import render

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import StadionSerializer, MatchSerializer, ParticipingSerializer, \
    TeamSerializer
from stadion.models import Stadion
from matches.models import Match, Participing
from team.models import Team


class StadionDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = StadionSerializer
    queryset = Stadion.objects.all()


class Stadions(ListCreateAPIView):
    serializer_class = StadionSerializer
    queryset = Stadion.objects.all()


class MatchDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()


class Matches(ListCreateAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()


class ParticipingDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipingSerializer
    queryset = Participing.objects.all()


class Participings(ListCreateAPIView):
    serializer_class = ParticipingSerializer
    queryset = Participing.objects.all()


class TeamDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class Teams(ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
