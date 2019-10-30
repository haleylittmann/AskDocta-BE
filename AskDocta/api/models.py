from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_doctor = models.BooleanField(default=False)
    is_registrar = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone = PhoneNumberField(blank=True, help_text="(include country code)")

class Request(models.Model):
    message = models.TextField();
    phonenumber = models.BigIntegerField();
    created_at = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        "Returns Name and "
        return '%s %s' % (self.first_name, self.last_name)

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    DOB = models.DateField();
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES);
    current_issue = models.CharField(max_length=255);
    start = models.CharField(max_length=255)
    PAIN_CHOICES = ((1,'1'), (2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'))
    severity = models.IntegerField(choices=PAIN_CHOICES);
    ALLERGY_CHOICES = (('N', 'None'),('L', 'Latex'),('P', 'Penicillin'),('A', 'Aspirin'),('I', 'Iodine'),('S', 'Shellfish'),('O', 'Other'))
    MED_HIST_CHOICES = (
        ('bleed', 'Bleeding Problems'),
        ('anemia', 'Anemia'),
        ('hbp', 'High blood pressure'),
        ('hd', 'Heart disease/heart attack'),
        ('af', 'Atrial Fibrillation'),
        ('pace', 'Pacemaker'),
        ('lung', 'Lung Disease'),
        ('copd', 'COPD/emphysema'),
        ('kd', 'Kidney disease'),
        ('liv', 'Liver disease'),
        ('hep', 'Hepatitis'),
        ('col', 'Colitis'),
        ('div', 'Diverticulitis'),
        ('ulc', 'Ulcers/GERD'),
        ('thy', 'Thyroid problems'),
        ('lup', 'Lupus'),
        ('arth', 'Arthritis'),
        ('gout', 'Gout'),
        ('park', 'Parkinson\'s'),
        ('stroke', 'Stroke/TIA'),
        ('seiz', 'Seizures'),
        ('DVT', 'Phlebitis/DVT (blood clot)'),
        ('ven', 'Venereal disease'),
        ('canc', 'Cancer'),
        ('asth', 'Asthma'),
        ('diab', 'Diabetes'),
        ('hiv', 'HIV or AIDS'),
        ('hc', 'High Cholesterol')
    )
    FAM_HIST_CHOICES = (
        ('hbp', 'High blood pressure'),
        ('hd', 'Heart disease/heart attack'),
        ('diab', 'Diabetes'),
        ('arth', 'Arthritis')
    )
    allergies = MultiSelectField(choices=ALLERGY_CHOICES)
    med_hist = MultiSelectField(choices=MED_HIST_CHOICES)
    fam_hist = MultiSelectField(choices=FAM_HIST_CHOICES)
    other_allergy = models.CharField(max_length=255)
    curr_meds = models.CharField(max_length=255);
    other_hist = models.CharField(max_length=255)
    fam_other_hist = models.CharField(max_length=255)
    SMOKE_OPT = (('N', 'None'),('F', 'Former'),('S', 'Some Days'),('M', 'Most/Every Day'))
    smoke = models.CharField(max_length=1, choices=SMOKE_OPT);
    ALC_OPT = (('N', 'None'),('O', 'Occasional'),('F', 'Frequent'))
    alc = models.CharField(max_length=1, choices=ALC_OPT);
    doctor = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='doctor', blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        "Returns Name and "
        return '%s %s' % (self.first_name, self.last_name)

# class Poll(models.model):
#     s3_link = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True);

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    