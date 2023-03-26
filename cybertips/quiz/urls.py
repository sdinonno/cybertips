from django.urls import path
from django.urls import path
from .views import quizpage_view

urlpatterns = [
    path('quiz/', quizpage_view, name='quiz')
]
