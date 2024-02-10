# from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
# def tasks_list(request: Request, *args, **kwargs) -> Response:
#     if request.method == 'POST':
#         serializer = ListTasksSerializer(data=request.data)
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#
#             return Response(
#                 status=status.HTTP_201_CREATED,
#                 data=serializer.data
#             )
#         else:
#             return Response(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data=serializer.errors
#             )
#     else:
#         tasks = Task.objects.all()
#
#         if tasks:
#             serializer = ListTasksSerializer(tasks, many=True)
#
#             return Response(
#                 status=status.HTTP_200_OK,
#                 data=serializer.data
#             )
#         else:
#             return Response(
#                 status=status.HTTP_204_NO_CONTENT,
#                 data=[]
#             )

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework import status


from apps.tasks.serializers import ListTasksSerializer, TaskInfoSerializer
from apps.tasks.models import Task


class TasksListAPIView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        tasks = Task.objects.all()

        if tasks:
            serializer = ListTasksSerializer(tasks, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = ListTasksSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


# class TaskDetailGenericView(RetrieveAPIView):
#     serializer_class = TaskInfoSerializer
#
#     def get_object(self):
#         task_id = self.kwargs.get("task_id")
#
#         task = get_object_or_404(Task, id=task_id)
#
#         return task


class TaskDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskInfoSerializer

    def get_object(self):
        task_id = self.kwargs.get("task_id")

        task = get_object_or_404(Task, id=task_id)

        return task

    def get(self, request, *args, **kwargs) -> Response:
        task = self.get_object()

        serializer = self.serializer_class(task)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request, *args, **kwargs) -> Response:
        task = self.get_object()

        serializer = self.serializer_class(task, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request, *args, **kwargs) -> Response:
        task = self.get_object()

        task.delete()

        return Response(
            status=status.HTTP_200_OK,
            data='Deleted'
        )
