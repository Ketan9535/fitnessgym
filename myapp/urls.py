
from django.urls import path
from myapp import views
from .import views


urlpatterns = [

    path('', views.show, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='userlogin'),
    path('user_logout/', views.user_logout, name='userlogout'),
    path('addmember/', views.add_member, name='addmember'),
    path('update/<int:id>/',views.update_member,name='updatemember'),
    path('contact/', views.contact, name='contact'),
    path('show/',views.show,name='show'),
    path('logout/',views.user_logout,name='logout'),
    path('delete_member/<int:id>/',views.delete_member,name='delete_member'),

    # search
    path('search/',views.search,name='search'),

    path('pagedetail/<int:id>',views.page_detail,name='pagedetail'),
    path('faq',views.faq_list,name='faq'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('view_enquiry/',views.view_enquiry,name='view_enquiry'),
    path('update_enquiry/<int:id>/',views.update_enquiry,name='update_enquiry'),
    path('delete_enquiry/<int:id>/',views.delete_enquiry,name='deleteenquiry'),
    #path('delete_enquiry',views.de)
    path('gallery',views.gallery,name='gallery'),
    path('gallerydetail/<int:id>',views.gallery_detail,name='gallery_detail'),
    path('viewmember/',views.view_member,name='view_member'),


    #Admin
    path('Adminlogin',views.Admin_Login.as_view(),name='Adminlogin'),
    # path('admin_homepage/',views.admin_homepage,name='admin_homepage'),
    # path('customer_homepage/',views.customer_homepage,name='customer_homepage')


    path('addplan/',views.add_plan,name='addplan'),
    path('viewplan/',views.view_plan,name='view_plan'),
    path('update_plan/<int:id>/',views.update_plan,name='updateplan'),
    path('delete_plan/<int:id>/',views.delete_plan,name='delete_plan'),
    path('addbooking/',views.add_booking.as_view(),name='addbooking'),
    path('showbooking/',views.view_booking.as_view(),name='showbooking'),
    path('delete_booking/<int:id>/',views.delete_booking,name='delete_booking'),


   

    
    
]
