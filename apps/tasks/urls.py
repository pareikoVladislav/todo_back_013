from django.urls import path

# from apps.tasks.views import tasks_list
from apps.tasks.views import TasksListAPIView, TaskDetailGenericView

# urlpatterns = [
#     path('', tasks_list)
# ]

urlpatterns = [
    path('', TasksListAPIView.as_view()),
    path('<int:task_id>/', TaskDetailGenericView.as_view())
]
