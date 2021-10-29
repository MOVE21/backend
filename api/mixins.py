from stadion.models import Position


def stadion_change(stadion, data):
    stadion.players.set(data["players"])
    stadion.matches.set(data["matches"])
    stadion.teams.set(data["teams"])
    pos = Position.objects.create(**data["position"])
    stadion.position = pos
    stadion.save()
    return stadion


def match_change(match, data):
    match.participings.set(data["participings"])
    match.time_holding = data["time_holding"]
    match.is_complete = data["is_complete"]
    match.save()
    return match


def participing_change(participing, data):
    participing.score = data["score"]
    participing.team = data["team"]


def team_change(team, data):
    team.code = data["code"]
    team.cap = data["cap"]
    team.name = data["name"]
    team.players.set(data["players"])
    team.save()
    return team
