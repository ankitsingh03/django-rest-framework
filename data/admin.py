from django.contrib import admin
from .models import Umpire, Deliveries, Matches


@admin.register(Matches)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'season', 'team1', 'team2')
    ordering = ['id']


@admin.register(Deliveries)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'batting_team', 'batsman', 'batsman_runs', 'total_runs')
    ordering = ['id']


@admin.register(Umpire)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality', 'first_officiated', 'last_officiated', 'Number_of_Matches')
    ordering = ['id']

# Register your models here.
# admin.site.register(Umpire)
# admin.site.register(Deliveries)
# admin.site.register(Matches, CourseAdmin)
