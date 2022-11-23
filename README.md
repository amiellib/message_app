# message_app

This is a Django REST framework api project

The project have user_api and message_api

user_api :

Functions:

login :  get user auth_token

Send json  

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

No exra data
Need auth token


messeges_api :

Functions:
all function need auth token to be sent to use

create_message :  send message to othe user

Send json  

{
    "receiver": "id",
    "subject": "subject",
    "body": "body"
}

get_all_messages_user  : get all the messages of the user(sent and received)

No exra data


get_all_unread_messages_user : get all the messages of the user received and did not read it

No exra data

read_message : read a message you have

{
   "id" : "id of the message"
}


delete_message : delete a msg from a user (if both users delete it the message will move to deleted_archive)

{
   "id" : "id of the message"
}

get_all_messages_archive : get all messages the both user delete the message(archive)

need to be admin

no exra data

delete_messages_archive : delete a message from the archive


{
   "id" : "id of the message"
}
