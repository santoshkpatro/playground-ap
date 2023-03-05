from django.contrib import admin
from django.urls import path

from todos.views import todo_list, todo_detail, todo_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/todos/create/", todo_create),
    path("api/todos/", todo_list),
    path("api/todos/<int:id>/", todo_detail),
]
