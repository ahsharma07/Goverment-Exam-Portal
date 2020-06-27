from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    mobile=models.CharField(max_length=12)
    user=models.ForeignKey(User,on_delete=models.CASCADE)