from django.contrib.auth.hashers import make_password, is_password_usable
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=180, null=True, blank=True)  
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'
    )
    
    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        if self.password and not is_password_usable(self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
