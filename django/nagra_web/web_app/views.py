from django.shortcuts import render,HttpResponse, redirect
from web_app import models

def index(request):
    
    return render(request,"index.html")
    

def form(request):

    if request.method=="POST":
        print("this is post  ")
        name=request.POST['name']
        clgname=request.POST['clgname']
        dob=request.POST['dob']
        branch=request.POST['branch']
        cgpa=request.POST['cgpa']
        
        print(name,clgname,dob,clgname,cgpa)
        ins = models.student(name=name,dob=dob,cgpa=cgpa,clgname=clgname,branch=branch)
        ins.save()
        
    return render(request,"templates/form.html")