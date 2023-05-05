from django.db import models

# Create your models here.
class Registration(models.Model):
    username=models.CharField(max_length=40,unique=True)
    first_name=models.CharField(max_length=60, null=True, blank=True) 
    last_name=models.CharField(max_length=60, null=True, blank=True)
    email=models.CharField(max_length=60,unique=True,verbose_name='email',null=True, blank=True)
    
    location=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    
    mobile_no=models.CharField(max_length=13)
    birth_place=models.CharField(max_length=30,null=True,blank=True)
    
    
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.username + " " + self.email

