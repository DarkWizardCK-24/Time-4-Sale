from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
   product_id = models.AutoField
   product_name = models.CharField(max_length=60)
   desc = models.CharField(max_length=300)
   image = models.FileField()
   pub_date = models.DateField()
   price = models.IntegerField()
   category = models.CharField(max_length=50)

   def __str__(self):
       return self.name

class Customer(models.Model):
   first_Name = models.CharField(max_length=50)
   last_Name = models.CharField(max_length=50)
   contact = models.IntegerField()
   email = models.EmailField()
   user_Name = models.CharField(max_length=50)
   password = models.CharField(max_length=50)

   def __str__(self):
       return self.name

class Order(models.Model):
   order_ID = models.AutoField
   product_ID = models.CharField(max_length=10)
   price = models.IntegerField()
   user_Name = models.CharField(max_length=50)
   contact = models.IntegerField()
   address = models.CharField(max_length=50)
   date = models.DateField()
   status = models.CharField(max_length=50)

   def __str__(self):
       return self.name
