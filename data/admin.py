from django.contrib import admin
from .models import Umpire, Deliveries, Matches


class CourseAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'season', 'team1', 'team2')


# Register your models here.
admin.site.register(Umpire)
admin.site.register(Deliveries)
admin.site.register(Matches, CourseAdmin)
