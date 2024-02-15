from rest_framework import serializers

from apps.categories.models import Category
from apps.statuses.models import Status
from apps.subtasks.serializers import SubTaskShortInfoSerializer
from apps.tasks.models import Task


class ListTasksSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Category.objects.all()
    )

    class Meta:
        model = Task
        fields = '__all__'


class TaskInfoSerializer(serializers.ModelSerializer):
    subtasks = SubTaskShortInfoSerializer(many=True, read_only=True)
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
