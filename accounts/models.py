from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates a new user
        """
        if not email:
            raise ValueError("This object requires an email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Email Address',
        unique=True
    )
    first_name = models.CharField(
        'First Name',
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        'Last Name',
        max_length=30,
        blank=True
    )
    date_joined = models.DateTimeField(
        'Date Joined',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Active',
        default=True
    )
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification_pin = models.IntegerField(default=0)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
