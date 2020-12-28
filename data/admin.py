from django.contrib import admin
from .models import Umpire, Deliveries, Matches


@admin.register(Matches)
class CourseAdmin1(admin.ModelAdmin):
    list_display = ('id', 'season', 'team1', 'team2')
    ordering = ['id']


@admin.register(Deliveries)
class CourseAdmin2(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'batting_team',
                    'batsman', 'batsman_runs', 'total_runs')
    ordering = ['id']


@admin.register(Umpire)
class CourseAdmin3(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality',
                    'first_officiated', 'last_officiated', 'Number_of_Matches')
    ordering = ['id']
