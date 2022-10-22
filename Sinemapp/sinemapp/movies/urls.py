from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("theaters", views.theaters, name="movies_in_theaters"),
    path("upcoming", views.upcoming, name="upcoming_movies"),
    path("<slug:slug>", views.movie_details, name="movie_details"),
    path("person/<slug:slug>", views.person_details, name="person_details"),
]