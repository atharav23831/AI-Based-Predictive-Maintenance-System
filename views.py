```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Question, Choice, Submission


def submit(request):
    if request.method == "POST":
        score = 0
        total_questions = Question.objects.count()

        for question in Question.objects.all():
            selected_choice_id = request.POST.get(
                f"question_{question.id}"
            )

            if selected_choice_id:
                selected_choice = Choice.objects.filter(
                    id=selected_choice_id,
                    question=question
                ).first()

                if selected_choice and selected_choice.is_correct:
                    score += 1

        submission = Submission.objects.create(
            score=score,
            total_questions=total_questions
        )

        return redirect(
            "show_exam_result",
            submission_id=submission.id
        )

    return redirect("home")


def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission,
        id=submission_id
    )

    return render(
        request,
        "exam_result.html",
        {"submission": submission}
    )
```
