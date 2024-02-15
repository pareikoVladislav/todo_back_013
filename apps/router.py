from django.urls import path, include

urlpatterns = [
    path('tasks/', include('apps.tasks.urls')),
    path('subtasks/', include('apps.subtasks.urls')),
    path('statuses/', include('apps.statuses.urls')),
    path('categories/', include('apps.categories.urls')),
    path('users/', include('apps.custom_user.urls')),
]
