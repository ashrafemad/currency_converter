from django.conf import settings
from django.db import models


class ActivityLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    convert_from = models.CharField(max_length=4)
    convert_to = models.CharField(max_length=4)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}, {self.convert_from} - {self.convert_to}, {self.count} Times'

    @classmethod
    def log(cls, user, convert_from, convert_to):
        log_entry, created = cls.objects.get_or_create(
            user=user, convert_from=convert_from, convert_to=convert_to
        )
        log_entry.count += 1
        log_entry.save()
