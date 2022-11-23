from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Messages, Messages_deleted_archive
from messages_api import serializers
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import  IsAdminUser
from rest_framework.decorators import  permission_classes
# Create your views here.

class messagesApiView(viewsets.ModelViewSet):
    """Messages API"""

    @action(methods=['post'], detail=False)
    def create_message(self, request, format=None):
        """Create a new message"""
        serializer = serializers.CreateMessageSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        msg = Messages( sender = request.user, 
        receiver = serializer.validated_data.get('receiver'),
        subject = serializer.data['subject'], body = serializer.data['body'])
        msg.save()
        return Response({'message': "the message was sent successfully "})


    @action(methods=['get'], detail=False)
    def get_all_messages_user(self, request):
        """get all the id of user messages that he have(sent and receive)"""
        qs_sender = Messages.objects.filter(sender = request.user)
        qs_sender  = qs_sender.filter(delete_sender = False)
        serializer = serializers.GetAllMessageSerializer(qs_sender, many=True)
        qs_receiver = Messages.objects.filter(receiver = request.user )
        qs_receiver  = qs_receiver.filter(delete_receiver = False)
        serializer_receiver = serializers.GetAllMessageSerializer(qs_receiver, many=True)
        return Response({'message_sent': serializer.data, 'message_receive': serializer_receiver.data})
        
    @action(methods=['get'], detail=False)
    def get_all_unread_messages_user(self,request ):
        """Get all messages that are unread of a user""" 
        qs_receiver = Messages.objects.filter(receiver = request.user )
        qs_receiver  = qs_receiver.filter(delete_receiver = False)
        qs_receiver = qs_receiver.filter(is_read = False)
        serializer_receiver = serializers.GetAllMessageSerializer(qs_receiver, many=True)
        return Response({'message_receive': serializer_receiver.data})


    @action(methods=['put'], detail=False)
    def read_message(self, request):
        """Read a message"""
        qs_sender = Messages.objects.filter(sender = request.user)
        qs_sender  = qs_sender.filter(id = request.data.get("id"))
        qs_sender = qs_sender.filter(delete_sender = False)
        serializer = serializers.ReadMessageSerializer(qs_sender ,many=True)
        if serializer.data == []:
            qs_receiver = Messages.objects.filter(receiver = request.user)
            qs_receiver  = qs_receiver.filter(id = request.data.get("id"))
            qs_receiver = qs_receiver.filter(delete_receiver  = False)
            serializer_receiver= serializers.ReadMessageSerializer(qs_receiver ,many=True)
            if serializer_receiver.data == []:
                return Response({'message':"Id was not found for this user"})
            #update/make sure the message mark as read to True
            message = Messages.objects.get(id=request.data.get("id"))
            message.is_read = True
            message.save()
            return Response({'message':serializer_receiver.data})
        else:
            return Response({'message':serializer.data})

    @action(methods=['put'], detail=False)
    def delete_message(self, request):
        """Delete a message"""
        qs_sender = Messages.objects.filter(sender = request.user)
        qs_sender  = qs_sender.filter(id = request.data.get("id"))
        qs_sender = qs_sender.filter(delete_sender = False)
        serializer = serializers.ReadMessageSerializer(qs_sender ,many=True)

        # message id was not as a sender
        if serializer.data == []:
            qs_receiver = Messages.objects.filter(receiver = request.user)
            qs_receiver  = qs_receiver.filter(id = request.data.get("id"))
            qs_receiver = qs_receiver.filter(delete_receiver  = False)
            serializer_receiver= serializers.ReadMessageSerializer(qs_receiver ,many=True)

            # message id was not as a receiver
            if serializer_receiver.data == []:
                return Response({'message':"Id was not found for this user"})

            #update/make sure the message mark as delete_reciver to True
            message = Messages.objects.get(id=request.data.get("id"))
            message.delete_receiver = True
            message.save()
        else:
            message = Messages.objects.get(id=request.data.get("id"))
            message.delete_sender = True
            message.save()
        if message.delete_receiver is True and message.delete_sender is True:
            #if delete_sender and delete_reciver True move message to Messages_deleted_arcive
            qs = Messages.objects.get(id =request.data.get("id") )
            Messages_deleted_archive.objects.create(sender_delete = qs.sender,
            receiver_delete = qs.receiver)
            Messages.objects.filter(id =request.data.get("id")).delete()
        return Response({'message':"Message deleted successfully message id was:"+ request.data.get("id")})


class MessagesDeletedApiView(viewsets.ViewSet):
    @permission_classes([IsAdminUser])
    @action(methods=['get'], detail=False)
    # @api_view(["GET"])
    def get_all_messages_archive(self, request):
        """Get all messages that archive """ 
        qs = Messages_deleted_archive.objects.all()
        serializer_receiver = serializers.GetAllArciveMessageSerializer(qs, many=True)
        return Response({'message': serializer_receiver.data})


    @permission_classes([IsAdminUser])
    @action(methods=['post'], detail=False)
    def delete_messages_archive(self, request):
        """Delete an archive message""" 
        id_return = request.data.get("id")
        qs = Messages_deleted_archive.objects.filter(id= id_return)
        serializer = serializers.DeleteArciveMessageSerializer(qs ,many=True)
        if serializer.data == [] :
            return Response({'message Error':"Id was not found in the DB"})
        Messages_deleted_archive.objects.filter(id =request.data.get("id")).delete()
        return Response({'message':"Message archive deleted successfully message id was:"+ id_return})