from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from todo.views import TodoViewSet

todo_list = TodoViewSet.as_view({"get": "list", "post": "create"})
todo_detail = TodoViewSet.as_view({"patch": "partial_update", "delete": "destroy"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userSystem.urls')),
    path('mypage/', include('mypage.urls')),

    url("^todo/$", todo_list, name="todo-list"),
    url("^todo/(?P<pk>[0-9]+)/$", todo_detail, name="todo-detail"),
]
