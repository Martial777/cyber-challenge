from django.shortcuts import render
from .models import Question

def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

def done_view(request):
    return render(request, 'done.html', {'score': 0})

def locked_view(request):
    return render(request, 'locked.html')

