from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError as err:
            raise ValueError(
                gettext_lazy(f"{err.message}.\nPlease, enter a valid email")
            )

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email=email)
        else:
            raise ValueError(gettext_lazy(
                "Email is required."
            ))

        if not first_name:
            raise ValueError(gettext_lazy(
                "First name is required."
            ))

        if not last_name:
            raise ValueError(gettext_lazy(
                "Last name is required."
            ))

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(
                gettext_lazy("Admin must be 'is staff'")
            )
        if not extra_fields.get("is_superuser"):
            raise ValueError(
                gettext_lazy("Admin must be a superuser")
            )

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)

        return user
