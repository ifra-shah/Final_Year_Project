from django.contrib import admin
from service.models import ServiceProvider
from service.models import login_form

class ServiceAdmin(admin.ModelAdmin):


  list_display=('skill','name','cnic','address','experience','worksample','coordinates')
admin.site.register(ServiceProvider,ServiceAdmin)
class LoginAdmin(admin.ModelAdmin):
  list_display=('role','name','email','password')
admin.site.register(login_form,LoginAdmin)

# Register your models here.
