from django.contrib import admin
from .models import Student_Profile

# Register your models here.
admin.site.register(Student_Profile)
admin.site.site_header = 'DreamWorks Admin'
admin.site.site_title = 'DreamWorks Admin'
admin.site.index_title = 'index'
