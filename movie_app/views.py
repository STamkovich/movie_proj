from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.views.generic import ListView, DetailView


# логика при помощи класса ListView
class ShowAllMovie(ListView):
    template_name = 'movie_app/all_movies.html'
    model = Movie
    context_object_name = 'movies'


# def show_all_movie(request):
#     # movies = Movie.objects.order_by('name', '-budget')
#     movies = Movie.objects.annotate(new_field_bool=Value(True))
#     agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
#     return render(request, 'movie_app/all_movies.html', {
#         'movies': movies,
#         'agg': agg,
#         'total': movies.count()
#     })

# логика при помощи класса DetailView
class ShowOneMovie(DetailView):
    template_name = 'movie_app/one_movie.html'
    model = Movie
    context_object_name = 'movie'


# логика при помощи функций
# def show_one_movie(request, slug_movie: str):
#     movie = get_object_or_404(Movie, slug=slug_movie)
#     directors = Director.objects.all()
#     return render(request, 'movie_app/one_movie.html', {
#         'movie': movie,
#         'directors': directors,
#     })

# логика при помощи класса ListView
class ShowAllDirectors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'director'


# логика при помощи функций
# def set_directors(request):
#     directors = Director.objects.all()
#     return render(request, 'movie_app/all_directors.html', {
#         'directors': directors,
#     })

# логика при помощи класса DetailView
class OneDirectors(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director
    context_object_name = 'directors'


# логика при помощи функций
# def one_directors(request, id_directors):
#     director = get_object_or_404(Director, id=id_directors)
#     return render(request, 'movie_app/one_director.html', {
#         'director': director
#     })

# логика при помощи класса ListView
class ShowAllActors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'


# логика при помощи функций
# def show_all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/all_actors.html', {
#         'actors': actors,
#     })

# логика при помощи класса DetailView
class OneActors(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'actor'

# логика при помощи функций
# def one_actor(request, id_actor):
#     actor = get_object_or_404(Actor, id=id_actor)
#     return render(request, 'movie_app/one_actor.html', {
#         'actor': actor,
#     })
