from django import forms
from api.models import User, Patient, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ProfileRoleForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('is_doctor', 'is_registrar')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone')

class PatientForm(forms.ModelForm):
    start = forms.CharField(required=False)
    other_allergy = forms.CharField(required=False)
    curr_meds = forms.CharField(required=False)
    other_hist = forms.CharField(required=False)

    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'height',
            'weight',
            'DOB',
            'sex',
            'current_issue',
            'start',
            'severity',
            'allergies',
            'other_allergy',
            'curr_meds',
            'med_hist',
            'other_hist',
            'fam_hist',
            'smoke',
            'alc'
        )