from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from decouple import config

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        message = '''
        Message: {}
        
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', [config('EMAIL')])
        messages.success(request, "Thank You For Contacting !")
    return render(request, "contact.html", {})
    