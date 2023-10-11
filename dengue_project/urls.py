
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from DENGUE_APP import views
urlpatterns = [
     path('', views.index,name="index"),
     path('protect/', views.protect,name="protect"),
     path('doctors/', views.doctors,name="doctors"),
     path('news/', views.news,name="news"),
     path('medicine/', views.medicine,name="medicine"),
     path('dashboard/', views.dashboard,name="dashboard"),
     path('addmedicine/', views.addmedicine,name="addmedicine"),
     path('medicinelist/', views.medicinelist,name="medicinelist"),
     path('adddoctor/', views.adddoctor,name="adddoctor"),
     path('doctorlist/', views.doctorlist,name="doctorlist"),
     path('addnews/', views.addnews,name="addnews"),
     path('newslist/', views.newslist,name="newslist"),
     path('savemedicine/', views.savemedicine,name="savemedicine"),
     path('med_data/', views.med_data,name="med_data"),
     path('delmed/<int:medicine_id>',views.delmed, name="delmed"),
     path('savedoctor/', views.savedoctor,name="savedoctor"),
    path('doclist/', views.doclist,name="doclist"),
    path('deldoctor/<int:doctor_id>',views.deldoctor, name="deldoctor"),
    path('savenews/', views.savenews,name="savenews"),
    path('newslist/', views.newslist,name="newslist"),
    path('signup/', views.saveuser,name="saveuser"),
    path('login/',views.loginuser,name="loginuser"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('admin/', admin.site.urls)
    
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)