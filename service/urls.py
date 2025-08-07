from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name='service'

urlpatterns=[
      path('form/',views.form,name='form'),
      path('customernoti/',views.CustomerNoti),
      path('portfolio/',views.portfolio),
      path('dash/',views.ProviderDash),
      path('services/',views.Services),
      path('c-dash/',views.CustomerDash),
      path('notification/',views.ProviderNotification),
      path('profile/',views.EditProfile),
      path('feedback/',views.CustomerFeedback),
      path('reviews/',views.CustomerReviews),
      path('bookingstatus/',views.BookingStatus),
      
      path('addservice/',views.AddService,name='add'),
      path('editservice/',views.EditService,name='edit'),
      path('deleteservice/', views.DeleteService, name='delete_service'),


      path('favourites/',views.Favourite),
      
      path('home/',views.home),
      path('ser/',views.browse),
      
      path('contact-us/',views.contact),   #Need to check css issues

      
      #Dont need
      path('livechat/',views.LiveChat),
      path('verification/',views.verification),
      path('logout/',views.logout),
      path('updatedpassword/',views.UpdatedPassword),
      path('login/',views.LoginForm),
]
