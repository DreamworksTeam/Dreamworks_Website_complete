from django.db import models

# Create your models here.
# model for careers
class Careers(models.Model):
    full_name = models.CharField(max_length = 500)
    email = models.EmailField()
    phone = models.CharField(max_length = 11)
    upload_cv = models.FileField(upload_to='documents/')

    class Meta:
        verbose_name = ('Career')
        verbose_name_plural = ('Careers')


    def __str__(self):
        return self.full_name

    