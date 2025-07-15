from django import forms

class ProviderForm(forms.Form):
    skill = forms.CharField(max_length=30)
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

    def clean_worksample(self):
        files = self.files.getlist('worksample')
        if len(files) < 3:
            print("❌ Please upload at least 3 work sample images.")
        return files

    def clean_cnic(self):
        cnic = self.cleaned_data['cnic']
        if not cnic.isdigit() or len(cnic) != 14:
            print("❌ Invalid CNIC. It must be exactly 14 digits.")
            return cnic