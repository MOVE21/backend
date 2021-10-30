from django.shortcuts import render

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from .serializers import StadionSerializer, MatchSerializer, ParticipingSerializer, \
    TeamSerializer, UserInviteSerializer, TeamInviteSerializer, UserSerializer, LoginByUsernameAndPasswordSerializer, \
    ProfileSerializer
from stadion.models import Stadion
from matches.models import Match, Participing
from team.models import Team
from profileapp.models import Profile
from invites.models import UserInvite, TeamInvite
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


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


class UserInviteDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserInvite.objects.all()
    serializer_class = UserInviteSerializer


class UserInvites(ListCreateAPIView):
    queryset = UserInvite.objects.all()
    serializer_class = UserInviteSerializer


class TeamInviteDetail(RetrieveUpdateDestroyAPIView):
    queryset = TeamInvite.objects.all()
    serializer_class = TeamInviteSerializer


class TeamInvites(ListCreateAPIView):
    serializer_class = TeamInviteSerializer
    queryset = TeamInvite.objects.all()


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(CreateAPIView):
    serializer_class = LoginByUsernameAndPasswordSerializer

    def create(self, request, *args, **kwargs):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        user = User.objects.get(username=request.POST["username"])
        print(request.POST, user, User.objects.all())
        if user is not None:
            return Response({"token": Token.objects.get(user=user).key})


class ProfileDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
