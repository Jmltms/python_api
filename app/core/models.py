from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for users."""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        if not email:
            raise ValueError('User must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class UserInfo(models.Model):
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return "%s %s" % (
            self.first_name,
            self.last_name
        )


class Product(models.Model):
    product_code = models.IntegerField(
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    stock_on_hand = models.IntegerField(
        null=True,
        blank=True
    )
    price = models.IntegerField(
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        db_index=True,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.SET_NULL,
        db_index=True,
        null=True,
        blank=True
    )
    quantity = models.IntegerField(
        null=True,
        blank=True
    )
    total = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product.name


class UserStock(models.Model):
    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.SET_NULL,
        db_index=True,
        null=True,
        blank=True
    )
    stock_holder = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    invested = models.IntegerField(
        null=True,
        blank=True
    )
    stock_value = models.IntegerField(
        null=True,
        blank=True
    )
