from todos.models import Todo
from huey.contrib.djhuey import task

@task()
def todo_archived(id):
    todo = Todo.objects.get(id=id)
    todo.status = Todo.Status.ARCHIVED
    todo.save()
