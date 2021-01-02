from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):

    return render(request, 'sendmail.html')

def sendmail(request):

    send_mail(
        'Test',
        'You are gay',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')
