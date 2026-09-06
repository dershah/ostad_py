from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You didn't enter any valid E-mail Address")

        email=self.normalize_email(email)
        user = self.model(email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.default('is_staff',True)
        extra_fields.default('is_active',True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=15, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email





# Create your models here.
# class user_registration(models.Model):
#     user_id= models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50)
#     email = models.EmailField(
#         max_length=254,
#         error_messages={'invalid': 'Enter a valid email address.'},
#         unique=True
#     )
#     password = models.CharField(max_length=128)