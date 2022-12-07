from django.urls import path
from .views import MovieView, MovieViewTest, MoviesOrderView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieViewTest.as_view()),
    path("movies/<int:movie_id>/orders/", MoviesOrderView.as_view()),
]
