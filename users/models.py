from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager


class User(AbstractUser):
    full_name = models.CharField(max_length=128, unique=True)
    phone_number = PhoneNumberField(unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    data_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "full_name"

    REQUIRED_FIELDS = ["phone_number"]

    objects = UserManager()

    def __str__(self):
        return self.full_name

    def tokens(self):
        pass
