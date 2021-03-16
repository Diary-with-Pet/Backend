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

    url("^todo/$", todo_list, name="todo-list"),
    url("^todo/(?P<pk>[0-9]+)/$", todo_detail, name="todo-detail"),

    url("^mypet/$", mypet_list, name="mypet-list"),
    url("^mypet/(?P<pk>[0-9]+)/$", mypet_detail, name="mypet-detail"),

    url("^diary/$", diary_list, name="diary-list"),
    url("^diary/(?P<pk>[0-9]+)/$", diary_detail, name="diary-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
