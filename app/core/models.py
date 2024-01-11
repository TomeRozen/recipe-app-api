"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
    BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Manager for user profiles.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create a new user profile.
        """
        if not email:
            raise ValueError('Users must have an email address.')

        # Normalize email address
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # Set password
        user.set_password(password)

        # Save user model
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and save a new superuser with given details.
        """
        user = self.create_user(email, password)

        # Set user as superuser
        user.is_superuser = True
        user.is_staff = True

        # Save user model
        user.save(using=self._db)

        return user

"""
It's a good idea to use custom user models for Django projects, as it is harder
to change later on. In addition, Django's built-in user model uses a username
field, which is not best practice for email-based authentication.
"""
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports using email instead of username.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Assign UserManager to objects attribute
    objects = UserManager()

    USERNAME_FIELD = 'email'