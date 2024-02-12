from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone

from apps.subtasks.models import SubTask
from apps.categories.models import Category
from apps.statuses.models import Status


class SubTaskShortInfoSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = SubTask
        fields = [
            'id',
            'title',
            'status',
            'deadline'
        ]


class ListSubTasksSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )
    creator = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all()
    )

    class Meta:
        model = SubTask
        fields = [
            'id',
            'title',
            'category',
            'status',
            'creator',
            'task',
            'date_started',
            'deadline',
        ]

    def validate_title(self, value):
        if value is None:
            raise serializers.ValidationError(
                "This field is required."
            )

        if len(value) > 75:
            raise serializers.ValidationError(
                "The title of subtask must be at maximum 75 symbols."
            )

        return value

    def validate(self, attrs: dict) -> dict:
        cur_datetime = timezone.now()
        date_started = attrs.get("date_started", None)
        deadline = attrs.get("deadline", None)

        if date_started is None or deadline is None:
            raise serializers.ValidationError(
                "You must provide both a date started and a deadline for the subtask you are creating."
            )

        if date_started < cur_datetime:
            raise serializers.ValidationError(
                "Date started can't be in the past."
            )

        if deadline < cur_datetime:
            raise serializers.ValidationError(
                "Deadline can't be in the past."
            )

        if deadline < date_started:
            raise serializers.ValidationError(
                "The deadline can't be earlier than the date started"
            )

        return attrs


class SubTaskInfoSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )
    creator = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all()
    )

    class Meta:
        model = SubTask
        fields = [
            'id',
            'title',
            'description',
            'category',
            'status',
            'creator',
            'date_started',
            'deadline'
        ]

    def validate_title(self, value):
        if self.instance and not value:
            value = self.instance.title

        if value is None:
            raise serializers.ValidationError(
                "This field is required"
            )

        if len(value) > 75:
            raise serializers.ValidationError(
                "The name of subtask must be at maximum 75 characters"
            )

        return value

    def validate_category(self, value):
        if self.instance and not value:
            value = self.instance.category

        if value is None:
            raise serializers.ValidationError(
                "You must specified the category of this subtask"
            )

        return value

    def validate_status(self, value):
        if self.instance and not value:
            value = self.instance.status

        if value is None:
            raise serializers.ValidationError(
                "You must specified the status of this subtask"
            )

        return value

    def validate_date_started(self, value):
        if self.instance and not value:
            value = self.instance.date_started

        if value < timezone.now():
            raise serializers.ValidationError(
                "Date started can't be in the past."
            )
        return value

    def validate_deadline(self, value):
        if self.instance and not value:
            value = self.instance.deadline

        if value < timezone.now():
            raise serializers.ValidationError(
                "The deadline can't be earlier than today."
            )

        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
