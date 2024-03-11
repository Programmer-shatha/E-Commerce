from django.db import models
from plants.models import Items
# Create your models here.
class ItemDetailsgifts(models.Model):  
    nameproduct=models.CharField(max_length=50 ,null=True)
    description=models.CharField(max_length=150) 
    image1=models.CharField(max_length=150)
    image2=models.CharField(max_length=150)
    image3=models.CharField(max_length=150)
    price=models.FloatField()   
    qty=models.IntegerField()    
    tax=models.FloatField()     
    total=models.FloatField()    
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE)
