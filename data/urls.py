from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home),
    path('prob1/', views.prob1, name='prob1'),
    path('prob2/', views.prob2, name='prob2'),
    path('prob3/', views.prob3, name='prob3'),
    path('prob4/', views.prob4, name='prob4'),
    path('team/', views.Team.as_view()),
    path('batsman/', views.Batsman.as_view()),
    path('umpire/', views.Umpires.as_view()),
    path('stacked/', views.Stacked.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
