from django.contrib import admin

from apps.subtasks.models import SubTask


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'task',
        'status',
        'creator',
        'date_started',
        'deadline'
    ]
    list_filter = [
        'category',
        'status',
        'date_started',
        'deadline'
    ]
    search_fields = [
        'title',
    ]

    def up_title_register(self, request, queryset):
        for obj in queryset:
            obj.title = obj.title.upper()
            obj.save()

    up_title_register.short_description = 'Поднять регистр'

    def down_title_register(self, request, queryset):
        for obj in queryset:
            obj.title = obj.title.lower()
            obj.save()

    down_title_register.short_description = ' Опустить регистр'

    actions = [
        'up_title_register',
        'down_title_register'
    ]

