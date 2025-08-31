from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to="Images/", null=False)

    # def __str__(self):
    #     return self.user.username
    

