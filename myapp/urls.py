from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('speech-to-text/', include('speech_to_text.urls')),
]
