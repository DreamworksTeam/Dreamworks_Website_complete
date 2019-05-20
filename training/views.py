from django.shortcuts import render, redirect
from .models import Training
from .forms import Registration
from django.contrib import messages

# Create your views here.

def training(request):
    training = Training.objects.all()
    context = {
        'trainings': training
    }
    return render(request, 'training/training.html', context)


def training_detail(request, id):
    training_detail = Training.objects.get(id= id)

    if request.method == 'POST':
        registration_form = Registration(request.POST)
       
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Submitted Successfully, We will get back to you shortly')
            return redirect('training')

    else:
        data = {'course': training_detail.title}
        registration_form = Registration(initial=data)

    context = {
        'training_detail': training_detail,
        'registration_form': registration_form
        }

    return render(request, 'training/training-detail.html', context)
