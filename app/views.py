from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from app.models import *
from django.http import HttpResponseRedirect

def topic_form(request):
    dt=Topic.objects.all()
    d={'dt':dt}
    if request.method=='POST':
        un=request.POST['topic']
        th=Topic.objects.get_or_create(Topic_name=un)[0]
        th.save()
        dt=Topic.objects.all()
        d={'dt':dt}
        return HttpResponseRedirect(reverse('topic_form'))
    return render(request,'topic_form.html',d)

def webpage_form(request):
    dt=Topic.objects.all()
    wpd=Webpage.objects.all()
    if request.method=='POST':
        tp=request.POST['tp']
        na=request.POST.get('na')
        ag=request.POST.get('ag')
        em=request.POST['em']
        TP=Topic.objects.get(Topic_name=tp)
        wd=Webpage.objects.get_or_create(Topic_name=TP,Name=na,Age=ag,Email=em)[0]
        wd.save()
        wpd=Webpage.objects.all()
        d={'wpd':wpd}
        return HttpResponseRedirect(reverse('webpage_form'))

    d={'dt':dt,'wpd':wpd}
    return render(request,'webpage_form.html',d)