from django.shortcuts import render
from .forms import Career_Form
from .models import Careers
from django.contrib import messages


# Create your views here.
def career(request):
    if request.method == 'POST':
        career_form = Career_Form(request.POST, request.FILES)

        if career_form.is_valid():
            # save 
            career_form.save()
            messages.success(request, 'Application Submitted Successfully')
       
    else:
        career_form = Career_Form()

    context = {
        'career_form': career_form
    }

    return render(request, 'careers/career.html', context)
