from django.db import models
import uuid
from user_api.models import UsersProfile
# Create your models here.


class Messages(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    sender = models.ForeignKey(UsersProfile,
     on_delete=models.SET_NULL, null=True, blank=True, related_name='sender')
    receiver = models.ForeignKey(UsersProfile,
     on_delete=models.SET_NULL, null=True, blank=True, related_name='receiver')
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    delete_sender = models.BooleanField(default=False)
    delete_receiver = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __UUID__(self):
        """Retrieve id of our messeage"""
        return self.id



class Messages_deleted_archive(models.Model):
    """After both users delete a message it will be store here for backup"""
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    sender_delete = models.ForeignKey(UsersProfile,
     on_delete=models.SET_NULL, null=True, blank=True, related_name='sender_delete')
    receiver_delete = models.ForeignKey(UsersProfile,
     on_delete=models.SET_NULL, null=True, blank=True, related_name='receiver_delete')
    created = models.DateTimeField(auto_now_add=True)


    def __UUID__(self):
        """Retrieve id of deleted messeage"""
        return self.id