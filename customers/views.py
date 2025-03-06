from django.shortcuts import render
from . models import Customer
# Create your views here.

def CustomerView(request):
    customers= Customer.objects.all()
    return render(request,'customers/customer.html',{'customers':customers})