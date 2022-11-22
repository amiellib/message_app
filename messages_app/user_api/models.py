from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token


class Users_manager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Crate a new user"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user = user)
        return user


    def create_superuser(self, email, name, password):
        """Crate a new superuser"""
        user = self.create_user(email, name, password, )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UsersProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length = 254, unique=True)#email if the want
    name = models.CharField(max_length=50)#full name 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = Users_manager() 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    
    def get_name(self):
        """Retrieve full name of a user"""
        return str(self.name)

    def get_id(self):
        """Retrieve id of a user"""
        return self.id
    
    def __str__(self):
        """Retrieve email of a user"""
        return self.email




