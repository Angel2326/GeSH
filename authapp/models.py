from django.contrib.auth.models import AbstractUser
from django.db import models


class New_user(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
# Create your models here.
