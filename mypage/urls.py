from django.urls import path

from mypage import views

urlpatterns = [
    path('list/', views.MyPageList.as_view()),
    path('update/<int:pk>/', views.MyPageUpdate.as_view()),
]
