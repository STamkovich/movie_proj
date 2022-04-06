from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movie(request):
    #movies = Movie.objects.order_by('name', '-budget')
    movies = Movie.objects.annotate(new_field_bool=Value(True))
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})
