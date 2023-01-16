from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def emailspage_view(request, *args, **kwargs):
    return render(request, "emails.html", {})