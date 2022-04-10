from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movie(request):
    # movies = Movie.objects.order_by('name', '-budget')
    movies = Movie.objects.annotate(new_field_bool=Value(True))
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    directors = Director.objects.all()
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
        'directors': directors,
    })


def set_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors,
    })


def one_directors(request, id_directors):
    director = get_object_or_404(Director, id=id_directors)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
    })


def one_actor(request, id_actor):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor,
    })
