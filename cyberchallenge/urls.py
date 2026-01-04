from django.contrib import admin
from django.urls import path
from users.views import register
from quiz.views import quiz_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', quiz_view, name='quiz'),
]
