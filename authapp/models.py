from django.db import models

from django.contrib.auth.models import  AbstractUser

class New_user(AbstractUser):
    image = models.ImageField(upload_to='users_mages', blank=True)
# Create your models here.
