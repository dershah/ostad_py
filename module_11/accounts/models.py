from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("No email Address entered!")

        email =self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        OWNER = 'OWNER', 'Owner'
        TENANT = 'TENANT', 'Tenant'

    first_name = models.CharField(max_length=50, blank=True)
    last_name  = models.CharField(max_length=50, blank=True)
    email      = models.EmailField(unique=True)
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.TENANT,
        db_index = True,
        )
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    @property
    def is_owner(self) -> bool:
        return self.role == self.Role.OWNER

    @property
    def is_tenant(self) -> bool:
        return self.role == self.Role.TENANT

    def __str__(self):
        return self.email
