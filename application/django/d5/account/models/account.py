from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    key = models.UUIDField()
    primary_email = models.EmailField()
    display_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'account'
