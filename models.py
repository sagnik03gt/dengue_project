from django.db import models

# Create your models here.

class Medicine(models.Model):
    medicine_name=models.CharField(max_length=100)
    medcine_about=models.CharField(max_length=100)
    medicine_cost=models.DecimalField(max_digits=5,decimal_places=2)
    medicine_img=models.ImageField(upload_to="medicine_img/")
    medicine_des=models.CharField(max_length=500)
    
    
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=100)
    specialist=models.CharField(max_length=100)
    doctor_fees=models.DecimalField(max_digits=5,decimal_places=2)
    doctor_schedule=models.CharField(max_length=50)
    doctor_img=models.ImageField(upload_to="doctor_img/")
    doctor_loc=models.CharField(max_length=500)
    
class News(models.Model):
    news_head=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    news_img=models.ImageField(upload_to="news_img/")
    date=models.DateField(null=True, blank=True)
    news_link=models.CharField( max_length=500)
    news_des=models.CharField(max_length=2000)
    
class userlog(models.Model):
    username=models.CharField(max_length=500)
    password=models.CharField(max_length=100)