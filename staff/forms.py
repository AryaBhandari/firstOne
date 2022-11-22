from django import forms
from .models import Staff
class StaffCreationForm(forms.ModelForm):
    username= forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    fullname = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    phoneno = forms.CharField(label='Phone Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    permanentaddress = forms.CharField(label='Permanent Address',widget=forms.TextInput(attrs={'class':'form-control'}))
    dob = forms.DateField(label='Date of Birth',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model = Staff
        exclude=['joindate','user']

