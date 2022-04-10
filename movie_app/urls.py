from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.set_directors, name='name-director'),
    path('directors/<int:id_directors>', views.one_directors, name='directors-ditail'),
    path('actors', views.show_all_actors),
    path('actors/<int:id_actor>', views.one_actor, name='actor-ditail'),


]
