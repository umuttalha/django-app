from ast import keyword
from pyexpat.errors import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect,render,HttpResponse,get_object_or_404
from matplotlib.style import context
from django.contrib.auth.decorators import login_required
#import informations
from .models import Information
from .forms import InfoForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def informations(request):

    keyword = request.GET.get("keyword")

    if keyword:
        informations = Information.objects.filter(Q(content__contains = keyword) | Q(title__contains = keyword))
        context={
            "informations":informations
        }
        return render(request,"informations.html",context)


    informations = Information.objects.all()
    context={
        "informations":informations
    }
    return render(request,"informations.html",context)

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    informations = Information.objects.filter(author = request.user)
    context={
        "informations":informations
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addinfo(request):
    form =InfoForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        information=form.save(commit=False)
        information.author = request.user
        information.save()

        messages.success(request,"Information successfully added")
        return redirect("informations:dashboard")



    return render(request,"addinfo.html",{"form":form})

def detail(request,id):
    information = get_object_or_404(Information,id=id)
    context={
        "information":information,
    }
    return render(request,"detail.html",context)

@login_required(login_url="user:login")
def updateInformation(request,id):
    information = get_object_or_404(Information,id=id)
    form = InfoForm(request.POST or None,request.FILES or None, instance=information)

    if information.author == request.user:
        if form.is_valid():
            information=form.save(commit=False)
            information.author = request.user
            information.save()

            messages.success(request,"Information successfully updated")
            return redirect("informations:dashboard")
    else:
        messages.info(request, "You are not authorized to update someone else's article.")
        return redirect("informations:dashboard")

    context={
        "form":form,
    }
    
    return render(request,"update.html",context)

@login_required(login_url="user:login")
def deleteInformation(request,id):
    information = get_object_or_404(Information,id=id)

    if information.author == request.user:
        information.delete()
        messages.success(request,"Information successfully deleted")
        return redirect("informations:dashboard")
    else:
        messages.info(request, "You are not authorized to delete someone else's article.")
        return redirect("informations:dashboard")


@login_required(login_url="user:login")
def addmylist(request):
    pass