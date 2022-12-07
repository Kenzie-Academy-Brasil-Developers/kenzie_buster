from django.urls import path
from .views import MovieView, MovieViewTest

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieViewTest.as_view()),
]
