from django.urls import path
from .views import TodoListView, TodoDetailView, TodoDeleteView, TodoCreateView, TodoUpdateView, TodoCompleteView

urlpatterns = [
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("todos/<int:id>", TodoDetailView.as_view(), name="todo_detail"),
    path("todos/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todos/<int:id>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
    path("todos/<int:id>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("todos/<int:id>/complete/", TodoCompleteView.as_view(), name="todo_complete"),
]
