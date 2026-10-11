```python
from django.contrib import admin
from .models import Question, Choice, Submission, Lesson

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'lesson')
    search_fields = ('question_text',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
```
