from django.conf.urls import url
from django.urls import path

from userSystem.views import hello

urlpatterns = [
    path('hello/', hello),
]
