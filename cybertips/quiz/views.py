from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import QuizUser, Question, Attempts


def quizpage_view(request, *args, **kwargs):
    QUser, created = QuizUser.objects.get_or_create()
    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')
        answered_question = QUser.attempts.select_related(
            'question').get(question__pk=question_pk)
        answer_pk = request.POST.get('answer_pk')

        try:
            chosen_option = answered_question.question.options.get(
                pk=answer_pk)
        except ObjectDoesNotExist:
            raise Http404

        QUser.validate_attempt(answered_question, chosen_option)
        return redirect('result', answered_question.pk)

    else:
        question = QUser.get_new_questions()
        if question is not None:
            QUser.create_attempt(question)

        context = {
            'question': question
        }

    return render(request, 'quiz.html', context)
