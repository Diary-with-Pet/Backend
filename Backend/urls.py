from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from diary.views import DiaryViewSet
from mypet.views import MyPetViewSet
from todo.views import TodoViewSet

todo_list = TodoViewSet.as_view({"get": "list", "post": "create"})
todo_detail = TodoViewSet.as_view({"patch": "partial_update", "delete": "destroy"})

mypet_list = MyPetViewSet.as_view({"get": "list", "post": "create"})
mypet_detail = MyPetViewSet.as_view({"patch": "partial_update", "delete": "destroy"})

diary_list = DiaryViewSet.as_view({"get": "list", "post": "create"})
diary_detail = DiaryViewSet.as_view({"patch": "partial_update", "delete": "destroy"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userSystem.urls')),
    path('mypage/', include('mypage.urls')),

    path('todo/', todo_list, name="todo-list"),
    path('todo/<int:pk>/', todo_detail, name="todo-detail"),

    path('mypet/', mypet_list, name="mypet-list"),
    path('mypet/<int:pk>/', mypet_detail, name="mypet-detail"),

    path('diary/', diary_list, name="diary-list"),
    path('diary/<int:pk>/', diary_detail, name="diary-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
