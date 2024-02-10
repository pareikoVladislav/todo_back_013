from rest_framework.viewsets import ModelViewSet

from apps.statuses.serializers import StatusesSerializer
from apps.statuses.models import Status


class StatusViewSet(ModelViewSet):
    serializer_class = StatusesSerializer
    queryset = Status.objects.all()
