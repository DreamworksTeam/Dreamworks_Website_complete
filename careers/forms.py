from django import forms 
from .models import Careers


# career form
class Career_Form(forms.ModelForm):
    class Meta:
        model = Careers
        fields = ('full_name', 'email', 'phone', 'upload_cv',)
        labels = {
            'upload_cv':'Upload your CV in pdf format'
        }