from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import uuid


# Create your models here.
class Product(models.Model):
   trek1=12000
   trek2=20000


   name=models.CharField(max_length=120)
   address=models.CharField(max_length=120)
   CATEGORIES = (
      ('kedarkantha', 'kedarkantha'),
      ('chopta/tungnath/deoriya tal', 'chopta/tungnath/deoriya tal'),
      ('Devkyara', 'Devkyara'),
      ('Har Ki Doon', 'Har Ki Doon'),
      ('Parashar Lake,Mandi', 'Parashar Lake,Mandi'),
      ('Karthik Swami', 'Karthik Swami'),
   )
   trek=models.CharField(max_length=120 ,choices=CATEGORIES)
   couponcode=models.CharField(max_length=5)
   id_proof=models.ImageField(upload_to='media/')
   height=models.CharField(max_length=120)
   weight=models.CharField(max_length=120)


   confirm=models.CharField(max_length=20 ,default="no")
   price =models.CharField(max_length=10)

class upi(models.Model):
   upiname=models.CharField(max_length=120)
   email=models.EmailField(max_length=120)
   transid=models.CharField(max_length=120)
   confirm=models.CharField(max_length=5,default="no")



##class Location1(models.Model):
  ## description=models.CharField(max_length=200,default="")
   ##magee=models.ImageField(upload_to='images/')

   ##def image_tag(self):
     # if self.imagee:
      #   return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.imagee.url)
      #else:
       #  return 'No Image Found'

   #image_tag.short_description = 'Image'

   #def __str__(self):
    #  return self.description


