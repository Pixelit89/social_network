from django.db import models
from django.db.models.signals import post_save

from main.models import ExtendedUser


class Thread(models.Model):
    participants = models.ManyToManyField(ExtendedUser)
    last_message = models.DateTimeField(null=True, blank=True, db_index=True)


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(ExtendedUser)
    thread = models.ForeignKey(Thread)
    datetime = models.DateTimeField(auto_now_add=True, db_index=True)


def update_last_message_datetime(sender, instance, created, **kwargs):
    if not created:
        return

    Thread.objects.filter(id=instance.thread.id).update(
        last_message=instance.datetime
    )


post_save.connect(update_last_message_datetime, sender=Message)