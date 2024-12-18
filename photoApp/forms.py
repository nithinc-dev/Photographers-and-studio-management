from django import forms
from .models import Photographer, Studio, Appointment, Service, Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'area', 'district', 'state', 'country']

class StudioForm(forms.ModelForm):
    street = forms.CharField(max_length=100)
    area = forms.CharField(max_length=100)
    district = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = Studio
        fields = ['name', 'email', 'phone_num', 'employees', 'services', 'street', 'area', 'district', 'state', 'country']
    
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # If editing an existing studio, populate address fields
            self.fields['street'].initial = self.instance.address.street
            self.fields['area'].initial = self.instance.address.area
            self.fields['district'].initial = self.instance.address.district
            self.fields['state'].initial = self.instance.address.state
            self.fields['country'].initial = self.instance.address.country

    def save(self, commit=True):
        studio = super().save(commit=False)
        address, _ = Address.objects.get_or_create(
            street=self.cleaned_data['street'],
            area=self.cleaned_data['area'],
            district=self.cleaned_data['district'],
            state=self.cleaned_data['state'],
            country=self.cleaned_data['country']
        )
        studio.address = address
        if commit:
            studio.save()
            self.save_m2m()
        return studio









class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = ['name', 'license_no', 'experience_in_years', 'email', 'phone_number', 'studio']
        studio = forms.ModelChoiceField(
        queryset=Studio.objects.all(),
        widget=forms.Select,
        empty_label="Select Studio"
    )
        
        
# class StudioForm(forms.ModelForm):
#     class Meta:
#         model = Studio
#         fields = ['name', 'email', 'phone_num', 'employees','address', 'services']
#         services = forms.ModelMultipleChoiceField(
#         queryset=Service.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False  # Diseases are optional
#     )
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['address'] = AddressForm()
            
            
# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['street', 'area', 'district', 'state', 'country']
        
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['customer_name', 'email', 'studio', 'service']
        service = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  
        )
        
        studio = forms.ModelChoiceField(
        queryset=Studio.objects.all(),
        widget=forms.Select,
        empty_label="Select Studio"
      )
        

# class StudioSearchForm(forms.Form):
#      district = forms.forms.ModelChoiceField(
#         queryset=Address.objects.all(),
#         widget=forms.Select,
#         empty_label="Select district",
#         required=False
#     )
#      area = forms.ModelChoiceField(
#         queryset=Address.objects.all(),
#         widget=forms.Select,
#         empty_label="Select area",
#         required=False
#     )  
     
class StudioSearchForm(forms.Form):
    district = forms.CharField(max_length=100, required=False)
    area = forms.CharField(max_length=100, required=False)


# class StudioSearchForm(forms.Form):
#     district = forms.ModelChoiceField(
#         queryset=Address.objects.order_by('district').values_list('district', flat=True),
#         widget=forms.Select,
#         empty_label="Select district",
#         required=False
#     )
#     area = forms.ModelChoiceField(
#         queryset=Address.objects.order_by('area').values_list('area', flat=True),
#         widget=forms.Select,
#         empty_label="Select area",
#         required=False
#     )




