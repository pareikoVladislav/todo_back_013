from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.subtasks.serializers import ListSubTasksSerializer, SubTaskInfoSerializer
from apps.subtasks.models import SubTask


class ListSubtasksGenericView(ListCreateAPIView):
    serializer_class = ListSubTasksSerializer

    def get_queryset(self) -> list:
        subtasks = SubTask.objects.filter(
            creator=self.request.user.id
        )

        return subtasks

    def create_obj(self, data: dict) -> dict:
        serializer = self.serializer_class(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def get(self, request: Request, *args, **kwargs) -> Response:
        subtasks = self.get_queryset()

        if not subtasks:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=[]
            )

        serializer = self.serializer_class(subtasks, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def post(self, request: Request, *args, **kwargs) -> Response:
        new_subtask = self.create_obj(
            data=request.data
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data=new_subtask
        )


class SubTaskInfoGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskInfoSerializer

    def partly_update(self, instance: SubTask) -> dict:
        serializer = self.serializer_class(
            instance=instance,
            data=self.request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def full_update(self, instance: SubTask) -> dict:
        serializer = self.serializer_class(
            instance=instance,
            data=self.request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def get_object(self):
        subtask_id = self.kwargs.get("pk")

        subtask = get_object_or_404(SubTask, id=subtask_id)

        return subtask

    def get(self, request: Request, *args, **kwargs) -> Response:
        subtask = self.get_object()

        serializer = self.serializer_class(subtask)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs) -> Response:
        subtask = self.get_object()

        updated_subtask = self.full_update(
            instance=subtask
        )

        return Response(
            status=status.HTTP_205_RESET_CONTENT,
            data=updated_subtask
        )

    def patch(self, request: Request, *args, **kwargs) -> Response:
        subtask = self.get_object()

        updated_subtask = self.partly_update(
            instance=subtask
        )

        return Response(
            status=status.HTTP_205_RESET_CONTENT,
            data=updated_subtask
        )

    def delete(self, request: Request, *args, **kwargs) -> Response:
        subtask = self.get_object()

        subtask.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

