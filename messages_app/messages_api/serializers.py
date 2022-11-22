from rest_framework import serializers as rfs
from .models import Messages, Messages_deleted_archive

class CreateMessageSerializer(rfs.ModelSerializer):
    """Serializes a create message"""
    class Meta:
        model = Messages
        fields = ['receiver', 'subject', 'body']
        

class MessageSerializer(rfs.ModelSerializer):
    """Serializes a user"""
    class Meta:
        model = Messages
        fields = ['sender', 'receiver', 'subject', 'body', 'is_read', 'delete_sender', 'delete_receiver' , 'created', 'id']

class GetAllMessageSerializer(rfs.ModelSerializer):
    """Serializes a get all messages of a user"""
    class Meta:
        model = Messages
        fields = ['id']

class ReadMessageSerializer(rfs.ModelSerializer):
    """Serializes a message and read it """
    class Meta:
        model = Messages
        fields = [ 'id', 'sender', 'receiver', 'subject', 'body','created']


class DeleteMessageSerializer(rfs.ModelSerializer):
    """Serializes a message and read it """
    class Meta:
        model = Messages
        fields = [ 'sender', 'receiver']

class GetAllArciveMessageSerializer(rfs.ModelSerializer):
    """get all deleted messages"""
    class Meta:
        model = Messages_deleted_archive
        fields = ['id', 'sender_delete', 'receiver_delete', 'created']

class DeleteArciveMessageSerializer(rfs.ModelSerializer):
    """get all deleted messages"""
    class Meta:
        model = Messages_deleted_archive
        fields = ['id']