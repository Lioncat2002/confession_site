from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ConfessionForm

from base.models import Confessions
# Create your views here.
def Home(request):
    confessions=Confessions.objects.all()
    context={'confessions':confessions}
    return render(request,'home.html',context)

def confess(request):
    form=ConfessionForm()

    if request.method=='POST':
        form=ConfessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'confession_form.html',context)
