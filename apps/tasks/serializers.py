from rest_framework import serializers

from apps.subtasks.serializers import SubTaskInfoSerializer
from apps.tasks.models import Task


class ListTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskInfoSerializer(serializers.ModelSerializer):
    subtasks = SubTaskInfoSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    status = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    creator = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'category',
            'status',
            'creator',
            'subtasks',
            'deadline'
        ]
