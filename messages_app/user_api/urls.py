from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_api import views

urlpatterns = [
    path('api_users/', views.UserApiView.api_users , name = "api_users"),
    path('login/',views.UserApiView.login , name = "login" ),
    path('api-token-auth/', obtain_auth_token, name = "api-token-auth"),
    path('create_user/',views.UserApiView.create_user , name = "create_user" )

]