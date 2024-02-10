from rest_framework import serializers

from apps.statuses.models import Status


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Название статуса не должно быть меньше 3 символов"
            )
        if len(value) > 25:
            raise serializers.ValidationError(
                "Название статуса не должно превышать 25 символов"
            )

        return value
