from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, type, password=None):
        """
        Creates and saves a User with the given email, type and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            type=type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, type, password):
        user = self.create_user(
            email,
            password=password,
            type=type,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class ApiUser(AbstractBaseUser):
    type = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type']

    # Methods for admin site representation, if needed

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        if self.is_admin:
            return True

    def has_module_perms(self, api_app):
        # Does the user have permissions to view the app `api_app`?
        if self.is_admin:
            return True

