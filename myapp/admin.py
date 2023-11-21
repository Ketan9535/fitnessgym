from django.contrib import admin

# Register your models here.
from .models import AddMemberModel,Enquiry,Plan,GymBooking
from .import models

@admin.register(AddMemberModel)
class adminmember(admin.ModelAdmin):
    list_display =['id','name','contact','email','age','gender','plan','joindate','initialamount']


class BannerAdmin(admin.ModelAdmin):
    list_display=("alt_text","image_tag")
admin.site.register(models.Banners,BannerAdmin)    



class serviceAdmin(admin.ModelAdmin):
    list_display=("title","image_tag")
admin.site.register(models.service,serviceAdmin) 


class pageAdmin(admin.ModelAdmin):
    list_display=("title", )
admin.site.register(models.page,pageAdmin) 


class faqAdmin(admin.ModelAdmin):
    list_display=("quest", )
admin.site.register(models.faq,faqAdmin) 

class EnquiryAdmin(admin.ModelAdmin):
    list_display=("full_name","email","detail","send_time" )
admin.site.register(models.Enquiry,EnquiryAdmin) 


class GalleryAdmin(admin.ModelAdmin):
    list_display=("title","image_tag" )
admin.site.register(models.Gallery,GalleryAdmin) 


class GalleryImageAdmin(admin.ModelAdmin):
    list_display=("alt_txt","image_tag" )
admin.site.register(models.GalleryImage,GalleryImageAdmin) 


@admin.register(Plan)
class planadmin(admin.ModelAdmin):
    list_display =['name','amount','duration']

@admin.register(GymBooking)
class gymadmin(admin.ModelAdmin):
    list_display=['contact','email','plan','joindate','booking_for']


















