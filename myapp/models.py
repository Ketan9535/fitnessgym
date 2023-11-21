#from typing import Any
from django.db import models
from django.contrib.auth.models import User

from django.utils.html import mark_safe


# Create your models here.

class AddMemberModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default="")
    plan = models.CharField(max_length=50)
    joindate = models.DateField()
    initialamount = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Banners(models.Model):
    img=models.ImageField(upload_to="banners_imgs/")
    alt_text=models.CharField(max_length=150)
    class Meta:
        verbose_name_plural='1.Banners'
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'%(self.img.url))
    
    def __str__(self):
        return self.alt_text
    

class category(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to="cat_imgs/")
    class Meta:
        verbose_name_plural='2.Catogories'  


class service(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to="services/",null=True)

    def __str__(self):
        return self.title
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'%(self.img.url))
    

class page(models.Model):
    title=models.CharField(max_length=300)
    detail=models.TextField()

    def __str__(self):
        return self.title    
    

class faq(models.Model):
    quest=models.TextField()
    ans=models.TextField()

    def __str__(self):
        return self.quest    
    
    
 
class Enquiry(models.Model):
    full_name=models.CharField(max_length=400)
    email=models.CharField(max_length=400)
    detail=models.TextField()
    send_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name  
    

class Gallery(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to="gallery/",null=True)

    def __str__(self):
        return self.title
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'%(self.img.url))
       
    
class GalleryImage(models.Model):
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE)
    alt_txt=models.CharField(max_length=150)
    img=models.ImageField(upload_to="gallery_imgs/",null=True)

    def __str__(self):
        return self.alt_txt
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'%(self.img.url))
       


#class GymBooking(models.Model):
#    user=models.ForeignKey(User,related_name="user_booking",on_delete=models.CASCADE)
#    workout=models.ForeignKey(workout,on_delete=models.CASCADE)
#    joindate = models.DateTimeField(auto_now_add=True)


class Plan(models.Model):
    
    name=models.CharField(max_length=50)
    amount=models.FloatField()
    duration=models.IntegerField()


    def __str__(self):
        return self.name

class GymBooking(models.Model):
    booking_for=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    plan = models.CharField(max_length=50)
    joindate = models.DateField()


class GymTrainer(models.model):
    name=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    plan_type=models.CharField(max_length=30)
       



      
    
  
    





