from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from calculatorpro import settings


class Wallet(models.Model):
    Id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.FloatField(default="",null=True,blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)

