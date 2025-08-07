from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *


from django.contrib.auth.decorators import login_required
from service.decorators import provider_required


@login_required
def form(request):
    if request.method == 'POST':
        print(f'running {request.POST}')
        form = ProviderForm(request.POST, request.FILES)

        if form.is_valid():
            # skill = form.cleaned_data['skill']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            experience = form.cleaned_data['experience']
            coordinates = form.cleaned_data['coordinates']
            cnic = form.cleaned_data['cnic']
            worksample_files = request.FILES.getlist('worksample')  # Handle multiple files

            # Save each image as a separate entry
            for file in worksample_files:
                Provider.objects.create(
                    user = request.user,
                    name=name,
                    address=address,
                    experience=experience,
                    coordinates=coordinates,
                    cnic=cnic,
                    worksample=file,
                      
                )
            messages.success(request, "Form submitted successfully! You can create Your services here ")
            return redirect('service:add')
        else:
            print(f'the is {form.errors}')
            return render(request, "serviceprovider.html", {'form': form})
    else:
        form = ProviderForm()
        return render(request, "serviceprovider.html", {'form': form})

def form_creation(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES)

        if form.is_valid():
            skill = form.cleaned_data['skill']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            experience = form.cleaned_data['experience']
            coordinates = form.cleaned_data['coordinates']
            cnic = form.cleaned_data['cnic']
            worksample_files = request.FILES.getlist('worksample')  # Handle multiple files

            # Save each image as a separate entry
            for file in worksample_files:
                Provider.create(
                    skill=skill,
                    name=name,
                    address=address,
                    experience=experience,
                    coordinates=coordinates,
                    cnic=cnic,
                    worksample=file,
                      
                )
            return redirect('/verification')
        else:
            return render(request, "serviceprovider.html", {'form': form})
    else:
        form = ProviderForm()
        return render(request, "serviceprovider.html", {'form': form})

def verification(request):
    return render(request, "verificationcode.html")

def CustomerNoti(request):
    return render (render,"customernotification.html")
def portfolio(request):
    return render (request,"portfolio.html")
def contact(request):
    return render (request,"contact.html")
def logout(request):
    return render (request,"logout.html")
def UpdatedPassword(request):
    return render(request,"updatedpasswordform.html")


def ProviderDash(request):
    return render(request,"serviceproviderdashboard.html")

def CustomerDash(request):
    return render(request,"customerdashboard.html")

def Services(request):
    return render(request,"services.html")

def ProviderNotification(request):
    return render(request,"notification.html")
def EditProfile(request):
    return render(render,"editprofileform.html")
def CustomerFeedback(request):
    return render(render,"customerfeedback.html")
def LoginForm(request):
    return render(request,"login.html")
def CustomerReviews(request):
    return render(request,"customerreview.html")

def BookingStatus(request):
    return render(request,"servicebookingdetail.html")


@login_required
@provider_required
def AddService(request):
        print(request.user)
        if request.method == 'POST':
            print('inside the creation form')
            form = ProviderServiceForm(request.POST)

            if form.is_valid():
                service = form.save(commit=False)  # Don't save yet
                try:
                    provider = Provider.objects.get(user=request.user)  # Get Provider for current user
                    service.provider = provider
                    service.save()
                    messages.success(request, "Service added successfully.")
                    return redirect('service:add')
                except Provider.DoesNotExist:
                    messages.error(request, "You are not registered as a provider.")
            else:
                print(form.errors)
                messages.error(request, "Please fix the errors below.")
        else:
            cat = category.objects.all()
            try:
                provider = Provider.objects.get(user=request.user)
                services = ProviderService.objects.filter(provider=provider)
            except Provider.DoesNotExist:
                provider = None
                services = []

            
            context  = {
                'cat': cat,
                'services' : services            }
            
            return render(request,"addnewservice.html",context)


from django.shortcuts import get_object_or_404

def EditService(request):
    service_id = request.POST.get('service_id')
    service = get_object_or_404(ProviderService, id=service_id)

    if request.method == 'POST':
        form = ProviderServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, "Service updated successfully.")
            return redirect('service:add')

    return render(request, 'your-template.html', {'form': form})

def DeleteService(request):
    print('delete operation')
    service_id = request.POST.get('service_id')
    service = get_object_or_404(ProviderService, id=service_id)
    
    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully.")
        return redirect('service:add')  # 🔁 Update with your actual URL name
    
    # Optional: If you want to show confirmation page instead of using JS/modal
    return render(request, 'confirm_delete.html', {'service': service})
    
def LiveChat(request):
    return render(request,"messages.html")
def Favourite(request):
    return render(request,"favourite.html")

def home(request):
    return render(request,"index.html")

def browse(request):
    return render(request,"browseservices.html")