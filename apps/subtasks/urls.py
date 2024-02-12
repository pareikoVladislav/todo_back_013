from django.urls import path

from apps.subtasks.views import (
    ListSubtasksGenericView,
    SubTaskInfoGenericView,
)


urlpatterns = [
    path('', ListSubtasksGenericView.as_view()),
    path('<int:pk>/', SubTaskInfoGenericView.as_view()),
]
