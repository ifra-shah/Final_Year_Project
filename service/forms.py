from django import forms
from .models import *

class ProviderForm(forms.Form):
    # skill = forms.CharField(max_length=30)
    name = forms.CharField(max_length=50)
    cnic = forms.CharField(max_length=14)
    address = forms.CharField(max_length=50)
    experience = forms.IntegerField()
    worksample = forms.FileField()
    coordinates = forms.CharField(max_length=50)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip()) < 4:
            print("❌ Name must be at least 4 characters long.")
        return name

    # def clean_worksample(self):
    #     files = self.files.getlist('worksample')
    #     if len(files) < 3:
    #         print("❌ Please upload at least 3 work sample images.")
    #     return files

    def clean_cnic(self):
        cnic = self.cleaned_data['cnic'].strip()
        if not cnic.isdigit():
            raise forms.ValidationError("CNIC must contain only digits.")
        if len(cnic) != 13:  # or 14 if that's your format
            raise forms.ValidationError("CNIC must be exactly 13 digits.")
        return cnic

        
class ProviderServiceForm(forms.ModelForm):
    class Meta:
        model = ProviderService
        fields = ['service', 'name', 'price', 'description']
