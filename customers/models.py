from django.db import models

# Create your models here.
class Customer(models.Model):
    c_name = models.CharField(max_length=200)
    c_email = models.CharField(max_length=50)
    c_address = models.CharField(max_length=200)
    c_phone = models.CharField(max_length=12)

    def __str__(self):
        self.c_name

class Order(models.Model):
    o_id = models.IntegerField()
    o_name = models.CharField(max_length=100)
    o_quantity = models.IntegerField(max_length=20)
    o_time =models.TimeField()

    def __str__(self):
        self.o_name

