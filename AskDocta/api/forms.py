from django import forms
from api.models import User
from api.models import Patient
from api.models import Doctor

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'phone')

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'phone')


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name','last_name','DOB','sex','current_issue','length_of_issue','recent_changes','allergies')