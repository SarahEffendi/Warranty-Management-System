import dataclasses
from imaplib import _Authenticator
from multiprocessing import context
from telnetlib import LOGOUT
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from datetime import date, datetime
from warranty.models import Additem
from django.db.models import Q
 
# Create your views here.
def index(request):
    return render(request,'signin.html')

def home(request):
    return render(request,'home.html')    

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        #data = Additem.objects.filter(plno__icontains=q)
        multiple_q = Q(Q(plno__icontains=q) | Q(relatedplno__icontains=q) | Q(unifiedplno__icontains=q) )
        data = Additem.objects.filter(multiple_q)
        messages.success(request, 'Your Search Data is.')
    else:
      data = Additem.objects.all()
    context = {
            'data' : data
              }
    
    return render(request,'search.html',context)


def inventory(request):
    invent = Additem.objects.all()
    return render(request, 'inventory.html',{"invent":invent })

def additem(request):
    additem = Additem.objects.all()   # delete
    if request.method == "POST":
        plno = request.POST.get('plno')
        relatedplno = request.POST.get('relatedplno')
        unifiedplno = request.POST.get('unifiedplno')
        desc = request.POST.get('desc')                          
        aac = request.POST.get('aac')
        specno = request.POST.get('specno')
        gw = request.POST.get('gw')

        #object additem
        additem = Additem(plno=plno, relatedplno=relatedplno, unifiedplno=unifiedplno, desc=desc, aac=aac, specno=specno,gw=gw, date=datetime.today())
        additem.save()
        messages.success(request, 'items details has been successfully updated.')

    return render(request, 'additem.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
           login(request, user)
           fname = user.first_name 
           messages.success(request,"login Successfully.")
           return render(request,"home.html",{'fname' : fname} )
           

        else:
            messages.error(request,"Wrong Credentials!!")
            return redirect('signin')

    return render(request, 'signin.html')

def signup(request):

    if request.method=="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirmpassword= request.POST['confirmpassword']

        railwayuser = User.objects.create_user(username,email,password)
        railwayuser.first_name = fname
        railwayuser.last_name = lname

        railwayuser.save()

        messages.success(request,"Your Account has been Successfully Created.")

        return redirect('signin')


    return render(request, 'signup.html')

def signout(request):
    logout(request)
    messages.success(request," Logout Successfully.")
    return redirect('signin')


    #return HttpResponse("Inventary page"){% extends 'base.html' %}

 