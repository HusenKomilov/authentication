from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    def email_validator(self, email):
        if email:
            validate_email(email)
        else:
            raise ValueError("Bu yerda email validatsiyadamn o'tishi kerak")

    def create_user_email(self, full_name, email, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        if not full_name:
            raise ValueError("bu yerda ism-familiya bo'lishi kerak")
        user = self.model(full_name=full_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user_phone(self, full_name, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("bu yerda telefon raqam bo'lishi kerak")
        user = self.model(full_name=full_name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, full_name, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        user = self.create_user_phone(full_name=full_name, phone_number=phone_number, password=password, **extra_fields)
        user.save(using=self.db)
        return user

