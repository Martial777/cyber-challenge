from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question, Answer

@login_required
def quiz_view(request):
    if Answer.objects.filter(user=request.user).exists():
        return render(request, "locked.html")

    questions = Question.objects.all()

    if request.method == "POST":
        total = 0
        for q in questions:
            r = request.POST.get(f"question_{q.id}", "")
            score = 0
            for kw in q.keywords.split(","):
                if kw.lower() in r.lower():
                    score += 2
            Answer.objects.create(
                user=request.user,
                question=q,
                content=r,
                score=score
            )
            total += score
        return render(request, "done.html", {"score": total})

    return render(request, "quiz.html", {"questions": questions})
