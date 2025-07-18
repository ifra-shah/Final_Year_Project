from django.shortcuts import render, redirect
from .forms import ProviderForm
from .models import ServiceProvider


def form(request):
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
                ServiceProvider.objects.create(
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
    return render(request,"servicebookingdetails.html")
def AddService(request):
    return render(request,"addnewservice.html")
def LiveChat(request):
    return render(request,"messages.html")
def Favourite(request):
    return render(request,"favourite.html")