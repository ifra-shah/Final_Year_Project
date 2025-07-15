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
            return redirect('/thankYou/')
        else:
            return render(request, "serviceprovider.html", {'form': form})
    else:
        form = ProviderForm()
        return render(request, "serviceprovider.html", {'form': form})


def thankYou(request):
    return render(request, "thankYou.html")
