from django.db import models

from apps.categories.models import Category
from apps.statuses.models import Status
from apps.tasks.models import Task
from apps.custom_user.models import CustomUser


def get_first_status():
    return Status.objects.first()


class SubTask(models.Model):
    title = models.CharField(
        max_length=75
    )
    description = models.TextField(
        max_length=700,
        blank=True,
        null=True
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtasks',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET(get_first_status),
        null=True,
        blank=True
    )
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    date_started = models.DateTimeField()
    deadline = models.DateTimeField()
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.title[:8]}..."

    class Meta:
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
