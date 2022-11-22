from django import forms
from .models import Student,Education,Skill,month,Fee
class StudentCreationForm(forms.ModelForm):
    Username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fullname = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    fathersname = forms.CharField(label="Father's Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    mothersname = forms.CharField(label="Mother's Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    phoneno = forms.CharField(label='Phone Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    parentsno = forms.CharField(label="Parent's Number",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    permanentaddress = forms.CharField(label='Permanent Address',widget=forms.TextInput(attrs={'class':'form-control'}))
    dob = forms.DateField(label='Date of Birth',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    joindate = forms.DateField(label='Joined Date',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    profile= forms.ImageField(label='Profile Picture',required=False)
    class Meta:
        model = Student
        exclude=['user','roomno']

class EducationCreationForm(forms.ModelForm):
    course = forms.CharField(label='Course',widget=forms.TextInput(attrs={'class':'form-control'}))
    university = forms.CharField(label='University',widget=forms.TextInput(attrs={'class':'form-control'}))
    joinedYear = forms.DateField(label='Joined Year',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    passedYear = forms.DateField(label='Passed Year',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),required=False)
    class Meta:
        model = Education
        exclude = ['student']

class SkillCreationForm(forms.ModelForm):
    skills = forms.CharField(label='Skills',widget=forms.TextInput(attrs={'class':'form-control'}))
    level = forms.IntegerField(label='Level',widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Skill
        exclude = ['student']

class StudentEditForm(forms.ModelForm):
    fullname = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathersname = forms.CharField(label="Father's Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    mothersname = forms.CharField(label="Mother's Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phoneno = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    parentsno = forms.CharField(label="Parent's Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    permanentaddress = forms.CharField(label='Permanent Address',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(label='Date of Birth',
                          widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    roomno= forms.IntegerField(label='Room No.',widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Student
        exclude = ['user','username','joindate']


class PaidForm(forms.ModelForm):
    paidAt = forms.DateField(label='Paid on',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    month = forms.ChoiceField(choices=month,widget=forms.Select(attrs={'class':'form-control'}))
    amountPaid = forms.IntegerField(label='Amount',widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model= Fee
        exclude=['student']