from django.shortcuts import render,redirect    
from django.http import HttpResponse
from DENGUE_APP.models import Medicine,Doctor,News
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request, "index.html")

def protect(request):
    return render(request, "protect.html")

def news(request):
    news=News.objects.all()
    return render(request,"news.html",{"news_list":news})

def medicine(request):
    medicines=Medicine.objects.all()
    return render(request,"medicine.html",{"med_list": medicines})


def doctors(request):
    doctor=Doctor.objects.all()
    return render(request,"doctors.html",{"doc_list": doctor})

def dashboard(request):
    return render(request, "dashboard.html")

def addmedicine(request):
    return render(request, "addmedicine.html")

def medicinelist(request):
    return redirect("/med_data")
  

def adddoctor(request):
    return render(request, "adddoctor.html")

def doctorlist(request):
    return redirect("/doclist")

def addnews(request):
    return render(request, "addnews.html")

def newslist(request):
    return redirect('/newslist')

def savemedicine(request):
    if request.method=='POST':
        medname=request.POST.get('mname')
        medabout=request.POST.get('mfor')
        medcost=request.POST.get('mrs')
        medimg=request.FILES['mimg']
        meddes=request.POST.get('mdes')
        med_data=Medicine(medicine_name=medname,medcine_about=medabout,medicine_cost=medcost,medicine_img=medimg,medicine_des=meddes)
       
        med_data.save() 
        return redirect("/med_data")
   

def med_data(request):
    medicines=Medicine.objects.all()
    return render(request,"medicinelist.html",{"med_list": medicines})

def delmed(request,medicine_id):
    medicine=Medicine.objects.get(pk=medicine_id)
    medicine.delete()
    return redirect('/med_data')
    
    
def savedoctor(request):
    if request.method == 'POST':
        dname=request.POST.get('dname')
        dspe=request.POST.get('dspe')
        dfees=request.POST.get('dfees')
        dsche=request.POST.get('dsche')
        dimg=request.FILES['dimg']
        dloc=request.POST.get('dloc')
        doc_data=Doctor(doctor_name=dname,specialist=dspe,doctor_fees=dfees,doctor_schedule=dsche,doctor_img=dimg,doctor_loc=dloc)
        doc_data.save()
        return redirect("/doclist")
   
def doclist(request):
    doctor=Doctor.objects.all()
    return render(request,"doctorlist.html",{"doc_list": doctor})

def deldoctor(request,doctor_id):
    doctor=Doctor.objects.get(pk=doctor_id)
    doctor.delete()
    return redirect('/doclist')

def savenews(request):
    if request.method == 'POST':
        head=request.POST.get('nname')
        about=request.POST.get('nabt')
        img=request.FILES['nimg']
        date=request.POST.get('date')
        link=request.POST.get('nlink')
        des=request.POST.get('ndes')
        news_data=News(news_head=head,about=about,news_img=img,date=date,news_link=link,news_des=des)
        news_data.save()
        return redirect('/newslist')
    
def newslist(request):
    news=News.objects.all()
    return render(request,"newslist.html",{"news_list":news})

# def delnews(request):
#     news=News.objects.get(pk=news_id)
#     news.delete()
#     return redirect('/newslist')


def saveuser(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        #check for errorneous inputs
        if len(username) > 10:
            messages.error(request,"username must be in 10 characters")
            return redirect('index')
        
        if not username.isalnum():
            messages.error(request,"username should only contain letters or numbers")
            return redirect('index')
        
        #create user
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"your account is created")
        return redirect('index')
        
    else:
        return HttpResponse("error")
    
    
def loginuser(request):  
 if request.method == 'POST':
    loguser=request.POST.get('logusername')
    logpass=request.POST.get('logpassword')
    user=authenticate(request,username=loguser,password=logpass)
    
    if user is not None: 
        login(request, user)
        messages.success(request,"You are logged in")
        return redirect('index')
    else:
        messages.error(request,"invalid username and password")
    return HttpResponse('404-not found')

def logoutuser(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request,"You are logged out")
    return redirect('index')
    
    
        