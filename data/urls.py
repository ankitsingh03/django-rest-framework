from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home),
    path('api/', views.DataList.as_view()),
    path('api/<int:pk>', views.DataDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
