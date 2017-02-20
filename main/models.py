from django.db import models
from django.contrib.auth.models import User
class extended_user(User):
    avatar = models.ImageField(upload_to='/avatars/', default='/avatars/default.jpeg')