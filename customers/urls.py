from django.urls import path
from .views import CustomerView

urlpatterns = [
    path("customerinfo/", CustomerView, name="CustomerView"),
]
