from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)  # '1' -> sdjfhue8rb3457fgidysuif
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)



# class CustomUser(AbstractUser):
#     # username = models.CharField(max_length=50, unique=True, help_text=("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."))
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     # is_staff = models.BooleanField(default=False,help_text=("Designates whether the user can log into this admin site."))
#     is_active = models.BooleanField(default=False,help_text=("Designates whether this user should be treated as active. ""Unselect this instead of deleting accounts."))
#     username = None
#     # date_joined = models.DateTimeField(("date joined"), default=timezone.now)
#     activation_code = models.CharField(max_length=50, blank=True)
    
    # objects = UserManager()

    # EMAIL_FIELD = "email"
    # REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.email

    # def create_activation_code(self):
    #     import uuid
    #     code = str(uuid.uuid4())
    #     self.activation_code = code

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    username = None
    activation_code = models.CharField(max_length=50, blank=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
        
        
        
        