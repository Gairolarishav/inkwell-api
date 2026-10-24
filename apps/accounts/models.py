from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    role_choices = {
        "reader": "Reader",
        "author": "Author",
        "editor": "Editor",
        "admin": "Admin",
    }

    email = models.EmailField(unique=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="avatar/")
    role = models.CharField(choices=role_choices, default="reader")
    created_at = models.DateTimeField(auto_now=True)
