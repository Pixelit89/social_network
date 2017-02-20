from django.contrib import admin
from .models import ExtendedUser, Wall, Comments

admin.site.register((ExtendedUser, Wall, Comments, ))
# Register your models here.
