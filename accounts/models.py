from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from accounts.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Username"
    )

    first_name = models.CharField(
        max_length=64,
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=64,
        verbose_name="Last Name"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Email Address"
    )

    phone_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name="Is Staff"
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}'
