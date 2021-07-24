from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    t = [(1,'VGrapher'),(2,'User')]
    role = models.IntegerField(choices=t,default=1)
    studio_name = models.CharField(max_length=300, default='')
    vaddress = models.TextField(default='')
    experience = models.IntegerField(default=0)
    Description = models.TextField(default='')
    profileImag = models.ImageField(upload_to = 'ProfilePics/',default = 'ProfilePics/07.jpg')
    hadFilled = models.BooleanField(default=False)
    

class CamModels(models.Model):
    vgId = models.ForeignKey(User,on_delete=models.CASCADE)
    camName = models.CharField(max_length=100)
    prizePerHour = models.CharField(max_length=50)
    description = models.TextField(default='')
    camPic = models.ImageField(upload_to='CamaraPics/',default = 'CamaraPics/04.jpg')
    bookedDates = models.CharField(max_length=500,default="")

class OrderModel(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    cid = models.IntegerField()
    nameOfEvent = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=50)
    toDate = models.CharField(max_length=50)
    ceremonyTime = models.CharField(max_length=50)
    addressOfCeremony = models.TextField()
    t = [(1,'None'),(2,'Accept'),(3,'reject')]
    isAccepted = models.IntegerField(choices=t,default=1)
    email = models.EmailField()