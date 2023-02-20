from django.db import models


class Tip(models.Model):
    text = models.TextField(verbose_name='Tip title')

    def __str__(self) -> str:
        return super().__str__()


class TipDescription(models.Model):
    question = models.ForeignKey(
        Tip, related_name='tip', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Tip description')
