from django.db import models


# Create your models here.

class Training(models.Model):
    image = models.ImageField(upload_to = 'training')
    title = models.CharField(max_length = 30)
    subtitle = models.CharField(max_length = 100, null = True)
    duration = models.CharField(max_length = 10)
    tutor = models.CharField(max_length = 20, null = True)
    date = models.DateField(null = True)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    

    def __str__(self):
        return self.title


class Register(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    enquiries = models.TextField()
    course = models.CharField(max_length = 50, null = True)


    def __str__(self):
        return self.name

        

