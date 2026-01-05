from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('done/', views.done_view, name='done'),
    path('locked/', views.locked_view, name='locked'),
]

