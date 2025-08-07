from django.shortcuts import redirect
from .models import Provider
from django.contrib import messages



def provider_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            provider = Provider.objects.get(user=request.user)
        except Provider.DoesNotExist:
            messages.warning(request, "You need to become a provider before you can add services.")
            return redirect('service:form')  # Redirect to some error or signup page

        return view_func(request, *args, **kwargs)
    return wrapper
