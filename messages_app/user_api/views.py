from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from user_api.serializers import UsersSerializer, UserTokenSerializer, UserLoginSerializer, UserCreateSerializer
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

    @api_view(["POST"])
    @permission_classes([AllowAny])
    def login(request, *args, **kwargs):
        """Login to get the user Token
            username: is the email
            password: is the name
        """
        serializer = UserLoginSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        print(validated_data["email"])
        user = authenticate(request, username=validated_data["email"], password=validated_data["password"])
        serializer = UserTokenSerializer(user)
        print(user)
        return Response(serializer.data)    


    @api_view(["POST"])
    @permission_classes([AllowAny])
    def create_user(request):
        """create a user"""
        serializer = UserCreateSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        UsersProfile.objects.create_user(validated_data.get("email"), validated_data.get("name"))
        return Response( {"message": "User was created!  "})
        
