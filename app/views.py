from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def form(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        messages=request.POST['message']
        subject=name+" with email "+email+" sent you a mail !"
        send_mail(
            subject,
            messages,
            settings.EMAIL_HOST_USER,
            ['planettouchhealthcare@gmail.com'],
            fail_silently=False,
        )
    return render(request,'form.html')

def index(request):
    return render(request,'index.html')

def video(request):
    return render(request,'video.html')
