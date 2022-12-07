from django.urls import path
from . import views
from .views import LoginJWTView

urlpatterns = [
    path("users/", views.RegisterView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
]
