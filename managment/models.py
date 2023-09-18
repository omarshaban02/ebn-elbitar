from typing import Iterable, Optional
from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Product(models.Model):
    x = [
        ('prescription medications', 'prescription medications'),
        ('non-prescription medications', 'non-prescription medications'),
        ('beauty & cosmetics', 'beauty & cosmetics'),
        ('medical supplies', 'medical supplies'),
        ('baby and childcare prodects', 'baby and childcare prodects'),
    ]
    name = models.CharField(max_length=100, unique=True)
    id = models.IntegerField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expired_date = models.DateField()
    manufacture_date = models.DateField()
    description = models.TextField()
    supplier_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    supply_date = models.DateField()
    category = models.CharField(max_length=100, null=False, choices=x)
    image = models.ImageField(upload_to='prodects %y-%m-%d',null=True)
    image1 = models.ImageField(upload_to='prodects %y-%m-%d',null=True, blank= True)
    image2 = models.ImageField(upload_to='prodects %y-%m-%d',null=True, blank= True)
    quantity = models.IntegerField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['supply_date']


class User(models.Model):
    x = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    f_name = models.CharField(max_length=100, default='')
    m_name = models.CharField(max_length=100, default='')
    l_name = models.CharField(max_length=100, default='')
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=255)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=x, null=False)
    phone = models.CharField(max_length=11, unique=True)
    ssn = models.CharField(max_length=14, unique=True)
    # image = models.ImageField(upload_to='users %y-%m-%d')
    address = models.CharField(max_length=100, default='')

    
    def save(self):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save()

    class Meta:
        ordering = ['email']


class Cart(models.Model):

    id = models.CharField(primary_key=True, max_length= 5, unique=True)
    # order_date = models.DateTimeField()  # default= datetime
    order_total_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.00)
    product_item = models.ManyToManyField(Product, null=True)     # Omar Modification

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.id



class Customers(models.Model):
    x = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    f_name = models.CharField(max_length=100, default='')
    m_name = models.CharField(max_length=100, default='')
    l_name = models.CharField(max_length=100, default='')
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=255, editable= False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=x, null=False)
    phone = models.CharField(max_length=11, unique=True)
    ssn = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=100, default='')
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name} - {self.email}"

    def save(self):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save()



class Order(models.Model):
    x = [
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered'),
    ]
    id = models.CharField(primary_key=True, max_length=12, unique=True)
    order_date = models.DateTimeField()  # default= datetime
    order_total_price = models.DecimalField(max_digits=7, decimal_places=2)
    order_state = models.CharField(max_length=10, choices=x, null=False)
    customer_email = models.ForeignKey("Customers", on_delete=models.CASCADE)
    product_item = models.ManyToManyField(Product, null=True)     # Omar Modification

    class Meta:
        ordering = ['id']
