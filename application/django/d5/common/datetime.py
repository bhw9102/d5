import datetime

from django.utils import timezone


def to_aware(dt: datetime.datetime) -> datetime.datetime:
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        return timezone.make_aware(dt)
    return dt
