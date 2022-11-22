from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from user_api.serializers import UsersSerializer, UserTokenSerializer, UserLoginSerializer
from user_api.models import UsersProfile
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


class UserApiView(APIView):
    """ API View"""
    serialzier_class = UsersSerializer
    queryset = UsersProfile.objects.all()
    
    @api_view(["GET"])
    def api_users(request, *args, **kwargs):
        """
        Get all users 
        """
        qs = UsersProfile.objects.all()
        serializer = UsersSerializer(qs, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response({'users': serializer.data})

    @api_view(["GET","POST"])
    @permission_classes([AllowAny])
    def login(request, *args, **kwargs):
        """Login to get the user Token
            username: is the email
            password: is the name
        """
        serializer = UserLoginSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = authenticate(request, username=validated_data["email"], password=validated_data["password"])
        serializer = UserTokenSerializer(user)
        return Response(serializer.data)          
    