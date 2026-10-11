from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = Enrollment.objects.get(user=user, course=course)
    
    if request.method == 'POST':
        selected_ids = request.POST.getlist('choice')
        submission = Submission.objects.create(enrollment=enrollment)
        for choice_id in selected_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    total_score = 0
    grade = 0
    
    for question in course.question_set.all():
        total_score += question.grade
        selected_ids = [choice.id for choice in submission.choices.all() if choice.question == question]
        if question.is_get_score(selected_ids):
            grade += question.grade
            
    context['course'] = course
    context['grade'] = grade
    context['total_score'] = total_score
    context['submission'] = submission
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
