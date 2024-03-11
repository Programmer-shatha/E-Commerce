from django.db import models

# Create your models here.
class Items(models.Model): 
    name=models.CharField(max_length=50) 
    def __str__(self):
        return self.name


class ItemDetails(models.Model):  
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

class Cart(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    image=models.CharField(max_length=150,null=True)
    name_product=models.CharField(max_length=150,null=True)

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    credit_card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)


class invoice(models.Model):
    price=models.FloatField()
    tax=models.FloatField()
    total=models.FloatField()
    order= models.ForeignKey(Order, on_delete=models.CASCADE ,null=True)  
    created_at = models.DateTimeField(auto_now_add=True ,null=True)









