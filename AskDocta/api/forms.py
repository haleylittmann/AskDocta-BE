from django import forms
from api.models import User, Patient, Profile
import datetime

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

ISSUE_CHOICES = (
        (1,'Blood'), (2, 'Cancer'),(3, 'Cardiovascular/Heart'),(4, 'Ear'),(5, 'Eye'),(6, 'Infection'),(7, 'Immune'),(8, 'Injury/Accident'),
        (9, 'Mental Health'),(10, 'Metabolic/Endocrine'),(11, 'Muscle/Bone'),(12, 'Neurological'),(13, 'Oral and gastrointestinal'),
        (14, 'Renal and Urogenital'),(15, 'Reproduction/Childbirth'),(16, 'Respiratory'),(17, 'Skin'),(18, 'Stroke'),(19, 'General/Other')
    )

class SortForm(forms.Form):
    issue= forms.CharField(widget=forms.Select(choices=ISSUE_CHOICES))


class PatientForm(forms.ModelForm):
    start_int = 1900
    today = datetime.datetime.now()
    current_year = today.year
    year_choices =[]
    while start_int <= current_year:
        year_choices.append(start_int)
        start_int +=1
    DOB = forms.DateField(widget=forms.SelectDateWidget(years=year_choices))
    start = forms.DateField(required=False, widget=forms.SelectDateWidget(years=year_choices))
    start_details = forms.CharField(required=False)
    other_issue = forms.CharField(required=False)
    other_allergy = forms.CharField(required=False)
    curr_meds = forms.CharField(required=False)
    other_hist = forms.CharField(required=False)
    other_fam_hist = forms.CharField(required=False)

    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'height',
            'weight',
            'DOB',
            'sex',
            'issue',
            'other_issue',
            'start',
            'severity',
            'allergies',
            'other_allergy',
            'curr_meds',
            'med_hist',
            'other_hist',
            'fam_hist',
            'other_fam_hist',
            'smoke',
            'alc'
        )