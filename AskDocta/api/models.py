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




class Patient(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        "Returns Patient's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def get_profile(self):
        return 'Name: %s %s, Gender: %s, Age: %d, Weight: %d, Height: %d.' % (self.first_name, self.last_name, self.gender, self.age, self.weight, self.height)

    def get_doctor(self):
        return 'Doctor: %s' % (self.doctor_id)
