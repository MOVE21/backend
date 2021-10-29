from django.urls import path
from .views import StadionDetail, Stadions, MatchDetails, Matches, ParticipingDetails, \
    Participings, TeamDetails, Teams

urlpatterns = [
    path("stadion/<pk>", StadionDetail.as_view()),
    path("stadion", Stadions.as_view()),
    path("match/<pk>", MatchDetails.as_view()),
    path("match", Matches.as_view()),
    path("participing/<pk>", ParticipingDetails.as_view()),
    path("participing", Participings.as_view()),
    path("team/<pk>", TeamDetails.as_view()),
    path("team", Teams.as_view())
]
