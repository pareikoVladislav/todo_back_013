from django.contrib.auth.models import User
from django.db import models

from apps.categories.models import Category
from apps.statuses.models import Status
from apps.tasks.db_helpers import generate_default_title


class Task(models.Model):
    title = models.CharField(
        max_length=75,
        verbose_name='TASK NAME',
        default=generate_default_title,
        unique=True,
    )
    description = models.CharField(
        max_length=1000,
        default='Здесь может быть ваше описание к задаче',
        unique_for_date='date_started',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date_started = models.DateTimeField(
        help_text='ДАТА, КОГДА ЗАДАЧА БЫЛА СОЗДАНА',
        auto_now_add=True,
    )
    deadline = models.DateTimeField()
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.title[:8]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['date_started']
        unique_together = ('category', 'status', 'description')
        get_latest_by = 'date_started'
