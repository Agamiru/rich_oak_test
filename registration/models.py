from django.db import models

from django.contrib.auth.models import AbstractUser


from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=200)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bvn = models.IntegerField(unique=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"
        # verbose_name_plural = "users"