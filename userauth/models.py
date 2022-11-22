from django.db import models
from django.contrib.auth.models import User

status=[('rejected','Rejected'),('accepted','Accepted'),('pending','Pending')]
# Create your models here.
class SignupRequest(models.Model):
    status= models.CharField(choices=status,max_length=30,default=status[-1][1])
    user= models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.status
