from django.db import models
import random


class Question(models.Model):
    ALLOWED_ANSWERS = 1

    text = models.TextField(verbose_name='Question description')
    max_score = models.DecimalField(
        verbose_name='Maximum score', default=3, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.text


class Answer(models.Model):
    MAX_ANSWER = 4
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE)
    rightAnswer = models.BooleanField(
        verbose_name='Is it the right answer?', default=False, null=False)
    text = models.TextField(verbose_name='Answer description')

    def __str__(self):
        return self.text


class QuizUser(models.Model):
    total_score = models.DecimalField(
        verbose_name='Total Score', default=0, decimal_places=2, max_digits=2)

    def get_quiz_user(self):
        pass

    def create_attempt(self, question):
        attempt = Attempts(question=question, quizUser=self)
        attempt.save()

    def get_new_questions(self):
        answered_questions = Attempts.objects.filter(quizUser=self).values_list(
            'question_id', flat=True)
        rest_questions = Question.objects.exclude(pk__in=answered_questions)
        if not answered_questions.exists():
            return None
        return random.choice(rest_questions)

    def validate_attempt(self, answered_question, chosen_answer):
        if answered_question.question_id != chosen_answer.question_id:
            return

        answered_question.chosen_answer = chosen_answer
        if chosen_answer.rightAnswer is True:
            answered_question.rightAnswer = True
            answered_question.score = chosen_answer.question.max_score
            answered_question.answer = chosen_answer

        answered_question.save()


class Attempts(models.Model):
    quizUser = models.ForeignKey(
        QuizUser, on_delete=models.CASCADE, related_name='attempts')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, null=True)
    rightAnswer = models.BooleanField(
        verbose_name='Is this the right answer?', default=False, null=False)
    score = models.DecimalField(
        verbose_name='Score', default=0, decimal_places=2, max_digits=6)
