from django.db import models

# Create your models here.
class User(models.Model):
   user_id = models.AutoField(primary_key=True)
   number = models.IntegerField(unique=True)
   password = models.CharField(max_length=100,unique=True)


   def __str__(self):
    #    return self.number
    return str(self.number)



class Details(models.Model):
   details_id = models.AutoField(primary_key=True)
   user_id = models.ForeignKey(User,on_delete=models.CASCADE)
   mo_name = models.CharField(max_length=255)
   mo_bulding_no = models.CharField(max_length=255)
   mo_area = models.CharField(max_length=255)
   mo_city = models.CharField(max_length=255)
   mo_pincode = models.IntegerField(unique=True)
   mo_landmark = models.CharField(max_length=255)
   mo_mobile = models.IntegerField(unique=True)
   mo_email = models.EmailField(unique=True)
   mo_food_license_no = models.CharField(max_length=255)
   mo_food_serve = models.CharField(max_length=255) 
   mo_food_licence_photo = models.ImageField(upload_to='food_licences/', null=True, blank=True)   
   mess_images = models.ImageField(upload_to='mess_images/', null=True, blank=True)