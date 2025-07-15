from django.db import models
from django.core.validators import RegexValidator

class ServiceProvider(models.Model):
    skill=models.CharField(max_length=30)
    name =models.CharField(max_length=50)
    cnic=models.CharField(max_length=14,

   validators=[
    RegexValidator(
        regex=r'^\d{14}$',
        message='CNIC must be exactly 14 digits'
    )
   ],
   unique=True
   )
    address=models.TextField(max_length=50,unique=True)
    experience=models.IntegerField()
    worksample=models.ImageField(upload_to='worksamples/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    coordinates=models.CharField(max_length=50)
    def __str__(self):
        return self.name
        

# Create your models here.
class login_form(models.Model):
    role=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name
        