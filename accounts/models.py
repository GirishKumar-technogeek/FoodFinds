from django.db import models
import django
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        user = self.create_user(email,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

USER_TYPES = (('ShopOwners','ShopOwners'),('NormalUsers', 'NormalUsers'),('Users', 'Users'))

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True) 
    contact_number = models.CharField(max_length=25)
    user_type = models.CharField(max_length=255,choices=USER_TYPES,default='Users')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin