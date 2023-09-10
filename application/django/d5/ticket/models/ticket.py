import uuid

from django.db import models


class Ticket(models.Model):
    key = models.UUIDField()
    account_key = models.UUIDField()
    status = models.CharField()
    subject = models.TextField()
