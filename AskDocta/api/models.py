from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)

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
