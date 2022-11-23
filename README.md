# message_app

This is a Django REST framework api project

The project have user_api and message_api

user_api :

Functions:

login :  get user auth_token
send json  
{
    "email": "email",
    "password": "name"
}
create_user  : create a user
send json  
{
"email" : "email"
"name" : "name"
}

api_users : get all users
no exra data
need auth token
