
from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Make sure Course, Lesson, Enrollment are imported/defined appropriately in your app

class Question(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    question_text = models.TextField()
    grade = models.IntegerField(default=1)

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        selected_total = len(selected_ids)
        if all_answers == selected_correct and selected_total == all_answers:
            return True
        return False

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id} for Enrollment {self.enrollment.id}"
