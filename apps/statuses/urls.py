from rest_framework.routers import DefaultRouter

from apps.statuses.views import StatusViewSet


router = DefaultRouter()

router.register('', StatusViewSet)

urlpatterns = router.urls
