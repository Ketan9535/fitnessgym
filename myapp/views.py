
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .forms import UserForm, AddMemberForm,EnquiryForm,PlanForm,GymBookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import AddMemberModel,Enquiry,service,Plan,GymBooking
from .import models
from .import forms


# Create your views here.
    

def show(request):
    banners=models.Banners.objects.all()
    services=models.service.objects.all()[:3]
    return render(request,'home.html',{'banners':banners,'services':services})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, f'Register Successfully')
            return redirect('userlogin')

    else:
        fm = UserForm()
    return render(request, 'register.html', {'forms': fm})

class Admin_Login(View):

    def get(self, request):
        return render(request,'Adminlogin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f'{username} Login Succesfully')
            return redirect('home')
        else:
            messages.info(request, f'Invalid UserName or Password')
            return redirect('Adminlogin')
        
           



def user_login(request):
    if request.method == 'POST':

        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(request, username=uname, password=upass)
        if user is not None:
            login(request, user)
            messages.success(request, f'Successfully {uname} loggedin...')
            return redirect(to='home')
        else:
            messages.warning(request, f'something went wrong')
            return redirect(to='userlogin')

    else:
        fm = UserForm()
    return render(request, 'userlogin.html', {'fm': fm})


def user_logout(request):
    logout(request)
    messages.success(request,'Successfully logout.....')
    return redirect('home')


def add_member(request):
    if request.method == 'POST':
        fm = AddMemberForm(request.POST)
        if fm.is_valid():
            f=fm.save(commit=False)
            f.user=request.user
            f.save()
            messages.success(request, f'Member Add Successfully....')
            return redirect('home')
        else:
            messages.warning(request,f'Something Went Wrong...')
            return redirect(to='addmember')
    else:
        fm = AddMemberForm()
        return render(request, 'addmember.html', {'forms': fm})
    


def view_member(request):
    member=AddMemberModel.objects.all()
    d = {'member':member}
    return render(request,'view_member.html',d)



def update_member(request,id):
    if request.method=='POST':
        pi=AddMemberModel.objects.get(id=id)
        fm=AddMemberForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('view_member')

    else:
        pi=AddMemberModel.objects.get(id=id)
        fm=AddMemberForm(instance=pi)
        return render(request,'update.html',{'forms':fm}) 




 


def delete_member(request,id):
    member=AddMemberModel.objects.get(id=id)
    member.delete()
    return redirect('view_member')

def page_detail(request,id):
    page=models.page.objects.get(id=id)
    return render(request,'home.html',{'page':page})

# faq

def faq_list(request):
    faq=models.faq.objects.all()
    return render(request,'faq.html',{'faqs':faq})


def enquiry(request):
    msg=''
    if request.method=='POST':
        form=EnquiryForm(request.POST)
        if form.is_valid:
            form.save()
            msg='Data has been saved'
    form=forms.EnquiryForm
    return render(request,'enquiry.html',{'form':form,'msg':msg})

def view_enquiry(request):
    enq=Enquiry.objects.all()
    d = {'enq':enq}
    return render(request,'view_enquiry.html',d)

def update_enquiry(request,id):
    if request.method=='POST':
        pi= Enquiry.objects.get(id=id)
        fm=EnquiryForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('view_enquiry')
        
    else:
        pi=Enquiry.objects.get(id=id)
        fm=EnquiryForm(instance=pi)
        return render(request,'enquiry_update.html',{'forms':fm}) 



def delete_enquiry(request,id):
    member=Enquiry.objects.get(id=id)
    member.delete()
    return redirect('view_enquiry')


def gallery(request):
    gallery=models.Gallery.objects.all().order_by('-id')
    
    return render(request,'gallery.html',{'gallerys':gallery})




def gallery_detail(request,id):
    gallery=models.Gallery.objects.get(id=id)
    gallery_imgs=models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(request,'gallery_imgs.html',{'gallery_imgs':gallery_imgs,'gallery':gallery})

# search--------------------------------------------->
def search(request):
    if request.method == 'POST':
        search_post = request.POST['search']
        x = service.objects.filter(title__contains=search_post)
        return render(request,'search.html', {'x': x})

   

def add_plan(request):
    if request.method == 'POST':
        fm = PlanForm(request.POST)
        if fm.is_valid():
            f=fm.save(commit=False)
            f.user=request.user
            f.save()
            messages.success(request, f'Plan Add Successfully....')
            return redirect('home')
        else:
            messages.warning(request,f'Something Went Wrong...')
            return redirect(to='addplan')
    else:
        fm = PlanForm()
        return render(request, 'add_plan.html', {'forms': fm})
    

def view_plan(request):
    plan=Plan.objects.all()
    d = {'plan':plan}
    return render(request,'view_plan.html',d)



def update_plan(request,id):
    if request.method=='POST':
        pi=Plan.objects.get(id=id)
        fm=PlanForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('view_plan')

    else:
        pi=Plan.objects.get(id=id)
        fm=PlanForm(instance=pi)
        return render(request,'update_plan.html',{'forms':fm}) 


def delete_plan(request,id):
    plan=Plan.objects.get(id=id)
    plan.delete()
    return redirect('view_plan')


class add_booking(View):
    def get(self, request):
        fm = GymBookingForm()
        return render(request, 'add_booking.html', {'forms': fm})

    def post(self, request):
        fm = GymBookingForm(request.POST)
        if fm.is_valid():
            f=fm.save(commit=False)
            f.booking_for=request.user
           
            f.save()
            messages.success(request, f'Booking  Successfully....')
            return redirect('home')
        else:
            messages.warning(request,f'Something Went Wrong...')
            return redirect(to='addbooking')


class view_booking(View):
    def get(self,request):
        booking=GymBooking.objects.all()
        d = {'booking':booking}
        return render(request,'view_booking.html',d)
    


 
def delete_booking(request,id):
        booking=GymBooking.objects.get(id=id)
        booking.delete()
        return redirect('view_booking')



 


         












    

  
    


            
    
    
   
        
    


    




    