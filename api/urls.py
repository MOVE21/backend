from django.urls import path
from .views import StadionDetail, Stadions, MatchDetails, Matches, ParticipingDetails, \
    Participings, TeamDetails, Teams, UserInviteDetail, UserInvites, TeamInvites, TeamInviteDetail, Register, Login, \
    ProfileDetails

urlpatterns = [
    path("stadion/<pk>", StadionDetail.as_view()),
    path("stadion", Stadions.as_view()),
    path("match/<pk>", MatchDetails.as_view()),
    path("match", Matches.as_view()),
    path("participing/<pk>", ParticipingDetails.as_view()),
    path("participing", Participings.as_view()),
    path("team/<pk>", TeamDetails.as_view()),
    path("team", Teams.as_view()),
    path("user-invite/<pk>", UserInviteDetail.as_view()),
    path("user-invite", UserInvites.as_view()),
    path("team-invite/<pk>", TeamInviteDetail.as_view()),
    path("team-invite", TeamInvites.as_view()),
    path("register", Register.as_view()),
    path("login", Login.as_view()),
    path("profile/<pk>", ProfileDetails.as_view())
]
