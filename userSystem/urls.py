from django.urls import path

from userSystem import views

urlpatterns = [
    path('register/', views.create_user),
    path('login/', views.login),
]
