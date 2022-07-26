from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowAllMovie.as_view()),
    path('movie/<slug:slug>', views.ShowOneMovie.as_view(), name='movie-detail'),
    path('directors', views.ShowAllDirectors.as_view(), name='name-director'),
    path('directors/<int:pk>', views.OneDirectors.as_view(), name='directors-ditail'),
    path('actors', views.ShowAllActors.as_view()),
    path('actors/<int:pk>', views.OneActors.as_view(), name='actor-ditail'),


]
