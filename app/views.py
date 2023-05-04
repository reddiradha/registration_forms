from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from app.forms import *
# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST'and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            nsuo=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            nsuo.set_password(pw)
            nsuo.save()

            nspo=pfd.save(commit=False)
            nspo.username=nsuo
            nspo.save()
            send_mail('registratoin',
                      'registration successfull',
                      'reddiradha0@gmail.com',
                      [nsuo.email],
                      fail_silently=True)
            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('data is not valid')
    return render(request,'registration.html',d)