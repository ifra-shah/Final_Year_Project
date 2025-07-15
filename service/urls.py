from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name='service'
urlpatterns=[
path('form/',views.form,name='form'),
path('thankYou/',views.thankYou,name='thankYou'),
]
