from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),

]
