from django.urls import path
from messages_api.views import messagesApiView, MessagesDeletedApiView
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('messages', messagesApiView ,basename="messages")
router.register('messages_delete', MessagesDeletedApiView ,basename="messages_delete")


urlpatterns = [
    path('', include(router.urls)),
]