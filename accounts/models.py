# Create your models here.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email,  password=None, is_admin=False, is_staff=False,
                    national_id=None, phone=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not password:
            raise ValueError("Users must have a password")
        if not national_id:
            raise ValueError("Users must have a National id No.")
        if not phone:
            raise ValueError("Users must have a Phone No. ")
        user_obj = self.model(
            email=self.normalize_email(email),
            phone=phone,
            username=username,
            national_id=national_id,
            is_admin=is_admin,
            is_staff=is_staff,
        )
        user_obj.set_password(password)  # change user password

        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, email, national_id, phone, password=None, is_admin=True, is_staff=True, ):
        user_obj = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            phone=phone,
            national_id=national_id,
            is_admin=is_admin,
            is_staff=is_staff,
        )

        user_obj.save(using=self._db)
        return user_obj


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    national_id = models.CharField(max_length=25, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True, unique=True)
    is_active = models.BooleanField(default=True)  # can login
    is_staff = models.BooleanField(default=False)  # staff user non superuser
    is_admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'username'  # username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['email', 'national_id', 'phone']  # ['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
