from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

# student Profile
sex = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
marital_status = [
    ('Single', 'Single'),
    ('Married', 'Married'),
     ('Divorce', 'Divorce')
]

academic_qualification = [
    ('PHD', 'PHD'),
    ('MSC', 'MSC'),
    ('BSC', 'BSC'),
    ('SSCE', 'SSCE'),
    ('JSCE', 'JSCE')

]
session = [
    ('Morning (10 am)', 'Morning (10 am)'),
    ('Afternoon (12pm - 1pm)', 'Afternoon (12pm - 1pm)'),
]

disablities = [
     ('Yes', 'Yes'),
    ('No', 'No'),

]

class Student_Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile_pics')
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.CharField(max_length = 50)
    Email = models.EmailField()
    sex = models.CharField(choices = sex, max_length = 10)
    martial_status = models.CharField(choices = marital_status, max_length = 10)
    Date_of_birth = models.DateField()
    Place_of_birth = models.CharField(max_length = 100)
    Contact_Address = models.TextField()
    Phone_No = models.PositiveIntegerField()
    Phone_No_2 = models.PositiveIntegerField()
    Academic_qualification = models.CharField(choices = academic_qualification, max_length = 10)
    Next_of_kin = models.CharField(max_length = 50)
    Phone_No = models.PositiveIntegerField(help_text = 'Enter Phone Number of Next of Kin')
    Session = models.CharField(choices = session, max_length = 20)
    Disablities = models.CharField(choices = disablities, max_length =10)
    register_date = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name

    
