from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        ARCHIVED = 'ARCHIVED', 'Archived'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    status = models.CharField(
        max_length = 20,
        choices = Status.choices,
        default = Status.ACTIVE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='todos'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
