from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField(verbose_name='Question description')

    def __str__(self) -> str:
        return super().__str__()


class Answer(models.Model):
    MAX_ANSWER = 4
    question = models.ForeignKey(
        Question, related_name='questions', on_delete=models.CASCADE)
    rightAnswer = models.BooleanField(
        verbose_name='Is it the right answer?', default=False, null=False)
    text = models.TextField(verbose_name='Answer description')


class Attempts(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name='attempts')
    rightAnswer = models.BooleanField(
        verbose_name='Is this the right answer?', default=False, null=False)
    score = models.DecimalField(
        verbose_name='Score', default=0, decimal_places=2, max_digits=6)


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.DecimalField(
        verbose_name='Total Score', default=0, decimal_places=2, max_digits=2)
