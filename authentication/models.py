from django.contrib.auth.models import AbstractUser
from django.db import models
from follower.models import UserFollows


class User(AbstractUser):
    SUBSCRIBER = "SUBSCRIBER"

    profil_photo = models.ImageField(verbose_name="Photo de profil")
