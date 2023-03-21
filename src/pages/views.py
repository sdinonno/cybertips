from django.shortcuts import render
from django.http import HttpResponse
from hitcount.views import HitCountDetailView


def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def alertpage_view(request, *args, **kwargs):
    return render(request, "alert.html", {})
