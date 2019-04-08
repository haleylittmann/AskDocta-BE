from django import forms
from api.models import User
from api.models import Doctor

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'phone')