from django.urls import path
from .views import LoginJWTView, RegisterView, UserView

urlpatterns = [
    path("users/", RegisterView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("users/<int:user_id>/", UserView.as_view()),
]
