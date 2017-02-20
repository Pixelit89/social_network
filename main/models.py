from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(User):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    friends = models.ManyToManyField('self', related_name='friends', blank=True)


class Wall(models.Model):
    message = models.TextField(default=None)
    image = models.ImageField(default=None)
    author = models.ForeignKey(ExtendedUser)


class Comments(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(ExtendedUser)
    message = models.ForeignKey(Wall)
    pub_date = models.DateTimeField(auto_now=True)