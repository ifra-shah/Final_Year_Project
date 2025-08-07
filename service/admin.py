from django.contrib import admin
from service.models import *

class ServiceAdmin(admin.ModelAdmin):


  list_display=('name','cnic','address','experience','worksample','coordinates')
admin.site.register(Provider,ServiceAdmin)
admin.site.register(category)
admin.site.register(ProviderService)

class LoginAdmin(admin.ModelAdmin):
  list_display=('role','name','email','password')

# Register your models here.
