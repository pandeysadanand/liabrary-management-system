from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


def user_pre_save(sender, instance, *args, **kwargs):
    try:
        instance.password = make_password(instance.password)
        return instance
    except Exception as e:
        print(e)


pre_save.connect(user_pre_save, sender=User)
