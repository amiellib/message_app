from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from user_api import views

urlpatterns = [
    # path('post/', views.TestApiView.post, name = "post"),
    # path('get/', views.TestApiView.get, name = "get"),
    path('api_users/', views.UserApiView.api_users , name = "api_users"),
    path('login/',views.UserApiView.login , name = "login" )

]