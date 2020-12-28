from django.db import models


class Umpire(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    first_officiated = models.IntegerField()
    last_officiated = models.IntegerField()
    Number_of_Matches = models.IntegerField()


class Deliveries(models.Model):
    match_id = models.IntegerField()
    batting_team = models.CharField(max_length=50)
    batsman = models.CharField(max_length=50)
    batsman_runs = models.IntegerField()
    total_runs = models.IntegerField()


class Matches(models.Model):
    season = models.IntegerField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
