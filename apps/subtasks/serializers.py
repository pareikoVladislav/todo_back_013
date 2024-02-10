from rest_framework import serializers

from apps.subtasks.models import SubTask


class SubTaskInfoSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = SubTask
        fields = [
            'id',
            'title',
            'description',
            'status',
            'deadline'
        ]
