from django.db import models
import datetime
from django.contrib.auth.models import User
import os

def getfileName(request,filename):
    now_time=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename='%s%s'%(now_time,filename)
    return os.path.join('uploads/',new_filename)
# Create your models here.
class Catagory(models.Model):
    name = models.CharField( max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getfileName,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-show,1-hidden')
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField( max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getfileName,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-show,1-hidden')   
    Created_at=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
    
class OrderDetails(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    Medicine_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.FloatField()