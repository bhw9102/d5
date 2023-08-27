import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    key = models.UUIDField(default=uuid.uuid4())
    email = models.EmailField(_('email address'), unique=True)
    groups = models.ManyToManyField('auth.Group', related_name="account_groups")
    user_permissions = models.ManyToManyField('auth.Permission', related_name="account_permissions")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'account'
