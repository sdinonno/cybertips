from django.contrib import admin

from .models import Question, Answer, Attempts, QuizUser
from .forms import ChooseInlineFormset


class ChooseAnswerInline(admin.TabularInline):
    model = Answer
    can_delete = False
    max_num = Answer.MAX_ANSWER
    min_num = Answer.MAX_ANSWER
    formset = ChooseInlineFormset


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChooseAnswerInline, )
    list_display = ['text',]
    search_fields = ['text', 'questions__text']


class AttemptsAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'rightAnswer', 'score']

    class Meta:
        model = Attempts


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Attempts)
admin.site.register(QuizUser)
