from django.urls import path

from diary import views

urlpatterns = [
    path('post/', views.DiaryPostView.as_view()),
]