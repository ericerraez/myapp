from django.urls import path
from . import views

urlpatterns = [
    path('', views.speech_to_text_view, name='speech-to-text'),
]
