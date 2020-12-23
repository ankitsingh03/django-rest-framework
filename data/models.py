from django.db import models


# Create your models here.
class Umpire(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    first_officiated = models.IntegerField()
    last_officiated = models.IntegerField()
    Number_of_Matches = models.IntegerField()

    # def __str__(self):
        # return self.name

class Deliveries(models.Model):
    batting_team = models.CharField(max_length=50)
    batsman = models.CharField(max_length=50)
    batsman_runs = models.IntegerField()
    total_runs = models.IntegerField()


class Matches(models.Model):
    season = models.IntegerField()
#     city = models.CharField(max_length=50)
#     date = models.DateField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
#     toss_winner = models.CharField(max_length=50)
#     toss_decision = models.CharField(max_length=50)
#     result = models.CharField(max_length=50)
#     dl_applied = models.IntegerField()
#     winner = models.CharField(max_length=50)
#     win_by_runs = models.IntegerField()
#     win_by_wickets = models.IntegerField()
#     player_of_match = models.CharField(max_length=50)
#     venue = models.CharField(max_length=50)
#     umpire1 = models.CharField(max_length=50)
#     umpire2 = models.CharField(max_length=50)
#     umpire3 = models.CharField(max_length=50)
