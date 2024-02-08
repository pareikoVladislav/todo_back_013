from django.contrib import admin

from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'status',
        'creator',
        'date_started',
        'deadline'
    ]
    list_filter = [
        'category',
        'status',
        'date_started'
    ]
    search_fields = ['title', ]
