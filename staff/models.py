from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Staff(models.Model):
    fullname= models.CharField(max_length=50)
    phoneno= models.CharField(max_length=14)
    email= models.EmailField(max_length=50,null=True,blank=True)
    permanentaddress= models.CharField(max_length=60)
    dob = models.DateField()
    idcard = models.ImageField(upload_to='idcard/')
    joindate = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(null=True, blank=True,upload_to='staff/')


    def __str__(self):
        return self.fullname