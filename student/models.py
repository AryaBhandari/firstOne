from django.db import models
from django.contrib.auth.models import User
# Create your models here.
month = (('january','Jan') , ('feburary','Feb'),('march','March'),('april','April'),('may','May'),('june','June'),('july','July'),('august','Aug'),('september','Sept'),('october','Oct'),('november','Nov'),('december','Dec'))
class Student(models.Model):
    fullname= models.CharField(max_length=50)
    fathersname= models.CharField(max_length=50)
    mothersname= models.CharField(max_length=50)
    phoneno= models.CharField(max_length=14)
    parentsno= models.CharField(max_length=14)
    email= models.EmailField(max_length=50)
    permanentaddress= models.CharField(max_length=60)
    dob = models.DateField()
    idcard = models.ImageField(upload_to='idcard/')
    joindate = models.DateField()
    roomno= models.IntegerField(null=True,blank=True)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(null=True, blank=True,upload_to='student/')

    def __str__(self):
        return self.fullname

class Education(models.Model):
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    joinedYear = models.DateField()
    passedYear = models.DateField(null=True,blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.fullname


class Skill(models.Model):
    skills = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.fullname

    class Meta:
        unique_together = ('skills','student')


class Fee(models.Model):
    paidAt= models.DateField()
    month=models.CharField(max_length=10,choices=month)
    amountPaid=models.IntegerField()
    student= models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.fullname

