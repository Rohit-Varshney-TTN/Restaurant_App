from django.db import models
from owner.models import User
# Create your models here.

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    status = models.CharField(max_length=15, choices=STATUS, default='New')

    def __str__(self):
        return self.order_number
    

class OrderedFood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    fooditem = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()


    def __str__(self):
        return self.fooditem.food_title