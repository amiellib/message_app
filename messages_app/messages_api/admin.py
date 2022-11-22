from django.contrib import admin

from messages_api import models

# Register your models here.

admin.site.register(models.Messages)
admin.site.register(models.Messages_deleted_archive)
