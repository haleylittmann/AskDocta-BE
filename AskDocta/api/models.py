from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    phone = PhoneNumberField(blank=True, help_text="(include country code)")

    def __str__(self):
        "Returns Doctor's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def get_profile(self):
       return 'Name: %s %s, Gender: %s, Specialty: %s.' % (self.first_name, self.last_name, self.gender, self.specialty)

class Request(models.Model):
    message = models.TextField();
    phonenumber = models.BigIntegerField();
    created_at = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        "Returns Name and "
        return '%s %s' % (self.first_name, self.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.doctor.save()