from django.contrib import admin

from apps.statuses.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
