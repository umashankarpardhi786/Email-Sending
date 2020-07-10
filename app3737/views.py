from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail

from project3737.settings import EMAIL_HOST_USER

def sendmail(request):
    send_to = request.POST.get("to").split(",")
    send_to_subject = request.POST.get("subject")
    send_to_message = request.POST.get("message")


    send_mail(send_to_subject,send_to_message,EMAIL_HOST_USER,send_to)

    return HttpResponse("<h1> Mail Sent </h1>")