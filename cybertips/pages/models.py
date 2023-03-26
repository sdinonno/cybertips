from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Tip(models.Model):
    text = models.TextField(verbose_name='Tip title')

    def __str__(self) -> str:
        return super().__str__()


class TipDescription(models.Model):
    question = models.ForeignKey(
        Tip, related_name='tip', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Tip description')

class Category(models.Model):
    text = models.TextField(verbose_name='Category')
