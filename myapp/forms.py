from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from.models import AddMemberModel,Enquiry,Plan,GymBooking
from .import models

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Enter Location', widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.IntegerField(label='Enter Contact', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'location', 'contact', 'password1', 'password2']
        labels = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email',
            'location': 'Enter Location',
            'contact': 'Enter Contact',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        help_texts={
            "username":""
        }




class AddMemberForm(forms.ModelForm):
    class Meta:
        model =AddMemberModel 
        fields =['name','contact','email','age','gender','plan','joindate','initialamount']

        labels = {
            'name':'Enter the name',
            'contact':'Enter the contact',
            'email':'Enter the Emailid',
            'age':'Enter the age',
            'gender':'Enter the gender',
            'plan':'Enter the plan',
            'joindate':'Joindate',
            'Initialamount':'Amount',


        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'plan': forms.TextInput(attrs={'class': 'form-control'}),
            'joindate': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'initialamount': forms.NumberInput(attrs={'class': 'form-control'}),

        }



class AdminLogin(AuthenticationForm):
    username = forms.CharField(label='Username:',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter Password:',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'password':'Enter Password :'
        }



class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields=("full_name","email","detail",)

        labels = {
            'full_name':'Enter the name',
            'email':'Enter the Email',
            'detail':'Enter the Details',
            


        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            

        }


#class GymBooking(forms.ModelForm):
#    class Meta:
#        model=GymBooking

#        fields=("user","workout","joindate","gym")

#       labels = {
#            'full_name':'Enter the name',
#            'email':'Enter the Email',
#            'detail':'Enter the Details',
            

class PlanForm(forms.ModelForm):
    class Meta:
        model=Plan
        fields =['name','amount','duration']

        labels = {
            'name':'Enter the name',
            'amount':'Enter the amount',
            'duration':'Enter the duration',
            

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

class GymBookingForm(forms.ModelForm):
    class Meta:
        model=GymBooking
        fields =['contact','email','plan','joindate']
        labels ={
        
            'contact':'Enter the contact',
            'email':'Enter the emailid',
            'plan':'Enter the plan',
            'joindate':'Enter the join date'

        }
        widgets ={
           
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'plan':forms.TextInput(attrs={'class':'form-control'}),
            'joindate': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            

        }

