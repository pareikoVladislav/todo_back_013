from rest_framework import serializers

from apps.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = [
        #     'name'
        # ]

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError(
                "The category name must be at least 4 symbols"
            )

        if len(value) > 25:
            raise serializers.ValidationError(
                "The category name must be at maximum 25 symbols"
            )

        return value  # -> validated_data
