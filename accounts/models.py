from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class AccountManager(BaseUserManager):
    """Custom manager for the Accounts model."""

    def _create_user(self, email, password, **extra_fields):
        """Internal helper for creating users.

        Normalizes the email and sets the given password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Accounts(AbstractBaseUser, PermissionsMixin):
    """Custom user model using email as the unique identifier."""
    profile_photo = models.ImageField(
        verbose_name="Profile Image",
        upload_to="profiles/",
        width_field="profile_photo_width",
        height_field="profile_photo_height",
        default="profiles/profile_placeholder.jpg",
    )
    profile_photo_width = models.PositiveIntegerField(null=True, blank=True)
    profile_photo_height = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length = 50, blank = True)
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this user should be treated as active."
                  "Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField(default=timezone.now)
    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
