from django.db import models
from django.core.validators import RegexValidator
from security.models import *

class Provider(models.Model):
    user = models.ForeignKey(MyUser, null=True, blank=True, on_delete=models.CASCADE)
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
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
     
     

class category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name   
        
class ProviderService(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    service = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True, blank=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True,)


    class Meta:
        unique_together = ('provider', 'service')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.provider.name} - {self.service.name} (PKR {self.price})"


# Create your models here.
