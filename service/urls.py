from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name='service'

urlpatterns=[
      path('form/',views.form,name='form'),
      path('verification/',views.verification),
      path('customernoti/',views.CustomerNoti),
      path('portfolio/',views.portfolio),
      path('contact-us/',views.contact),
      path('logout/',views.logout),
      path('updatedpassword/',views.UpdatedPassword),
      path('dash/',views.ProviderDash),
      path('notification/',views.ProviderNotification),
      path('profile/',views.EditProfile),
      path('feedback/',views.CustomerFeedback),
      path('login/',views.LoginForm),
      path('reviews/',views.CustomerReviews),
      path('bookingstatus/',views.BookingStatus),
      path('addservice/',views.AddService),
      path('livechat/',views.LiveChat),
      path('favourites/',views.Favourite),

]
