
from django.contrib import admin
from django.urls import path
from django.urls import include
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
#    path("",views.home,name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
