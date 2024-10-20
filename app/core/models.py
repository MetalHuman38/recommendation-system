"""
Django Database Models.
"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from decimal import Decimal
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


# Create your models here.
class UserManager(BaseUserManager):
    """
    User Manager class.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a new user.
        """

        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a new superuser.
        """

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Movie(models.Model):
    """
    Movie model representing movies in the database.
    """
    movie_id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Ratings(models.Model):
    """
    Ratings model.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(Decimal('1.0')),
            MaxValueValidator(Decimal('5.0'))
        ]
    )
    timestamp = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        verbose_name_plural = 'Ratings'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user} rated {self.movie} {self.rating}"
