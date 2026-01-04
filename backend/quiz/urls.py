from django.urls import path
from . import views



urlpatterns = [
    path("", views.index_view, name="index"),
    path("quiz/", views.quiz_view, name="quiz"),
]
