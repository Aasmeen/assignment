from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('content_editor', 'Content Editor'),
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)

    @property
    def is_content_editor(self):
        return self.role == 'content_editor'

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.role == 'admin'
