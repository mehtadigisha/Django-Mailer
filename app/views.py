from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    subject = 'Django Mailer'
    message = 'Hi! There is a important message for you.'
    from_email = 'sendersgmail'
    recipient_list = ['recipient1@example.com', 'recipient2@example.com']

    send_mail(subject, message, from_email, recipient_list)

    # return HttpResponse('Email sent successfully')
    return render(request,'home.html')