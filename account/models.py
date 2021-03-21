from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, address, phone, is_staff=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have first name')
        if not last_name:
            raise ValueError('Users must have last name')
        if not last_name:
            raise ValueError('Users must have address')
        if not date_of_birth:
            raise ValueError('Users must have date of birth')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            address = address,
            is_staff = is_staff,
            phone = phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name='super',
            last_name='user',
            date_of_birth=datetime.now(),
            address='super user has no address',
            phone=0,
            is_staff=True,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email', max_length=60, unique = True)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    date_of_birth   = models.DateField(verbose_name='date of birth')
    address         = models.CharField(max_length=100)
    phone           = models.PositiveIntegerField(verbose_name='phone number')
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm):
         return True
    
    def has_module_perms(self, app_label):
        return True
