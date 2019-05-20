from django.shortcuts import render, redirect
from .forms import Contact_Form
from django.core.mail import send_mail as sm
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages


# Create your views here.

def contact(request):
    if request.method == 'POST':
        contact_form = Contact_Form(request.POST)
        if contact_form.is_valid():
            
            # get data
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            phone = contact_form.cleaned_data['phone']
            message = contact_form.cleaned_data['message']
            subject = ['New Contact']
            recipient = [settings.EMAIL_HOST_USER]

  
            # send email
            try:
                sm(subject, message, [email], recipient)

            except BadHeaderError:
                return HttpResponse('Invalid Header')
            contact_form.save()
            messages.success(request, 'Email Sent Successfully, We will get back to you shortly')
            return redirect('contact')



    else:
        contact_form = Contact_Form()

    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact/contact.html', context)

