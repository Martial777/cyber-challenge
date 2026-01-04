from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Bienvenue sur la page d'accueil du quiz")
    # Ou si vous avez un template :
    # return render(request, 'quiz/index.html')

def quiz_view(request):
    return HttpResponse("Page du quiz - Cyber Challenge")
    # Ou si vous avez un template :
    # return render(request, 'quiz/quiz.html')
