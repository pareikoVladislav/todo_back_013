from django.urls import path

from apps.custom_user.views import UserRegistrationGenericView


urlpatterns = [
    path("auth/register/", UserRegistrationGenericView.as_view()),
]
