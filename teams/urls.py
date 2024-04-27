from django.urls import path
from .views import TeamsView, TeamsDetailsView
from . import views

urlpatterns = [
    path("teams/", views.TeamsView.as_view()),
    path("teams/<int:id>/", views.TeamsDetailsView.as_view()),
]
