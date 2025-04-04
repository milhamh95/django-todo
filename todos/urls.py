from django.urls import path
from .views import TodoListView, TodoDetailView, TodoDeleteView, TodoCreateView, TodoUpdateView

urlpatterns = [
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("todos/<str:id>", TodoDetailView.as_view(), name="todo_detail"),
    path("todos/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todos/<str:id>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
    path("todos/<str:id>/update/", TodoUpdateView.as_view(), name="todo_update"),
]
