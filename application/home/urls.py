from django.contrib import admin
from django.urls import path
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.index,name="index"),
    path('', views.index, name="index"),
    path('loginuser/', views.loginuser),
    path('user_detail/', views.user_detail),
    path('loginout/', views.loginout),
    path('about/', views.about),
    path('contact/', views.contact,name="contact"),
    path('services/', views.services),
    path('company_certification/', views.company_certification),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 





