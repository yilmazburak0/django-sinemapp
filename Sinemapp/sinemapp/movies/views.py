from datetime import date
from os import cpu_count
from time import perf_counter
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Movie



def index(request):
    released_movies = Movie.objects.filter(is_released=True)
    return render(request,"home-page.html",{
        'movies':released_movies,
    })


def theaters(request):
    released_movies = Movie.objects.filter(is_released=True)
    return render(request,"theaters.html",{
        'movies':released_movies,
    })


def upcoming(request):
    coming_movies = Movie.objects.filter(is_coming=True)
    return render(request,"upcoming.html",{
        'coming_movies': coming_movies,
    })


def movie_details(request,slug):
    movie = get_object_or_404(Movie, slug=slug)
    
    return render(request,"movie-details.html",{
        'movie':movie,
        'genres':movie.genres.all(),
        'people':movie.people.all(),
        "videos": movie.video_set.all(),
        
    })


def person_details(request,slug):
    person = get_object_or_404(Movie, slug=slug)
    
    return render(request,"person-details.html",{
        'person':person,
        
    })