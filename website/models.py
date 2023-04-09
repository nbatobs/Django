from django.db import models

# Create your models here.

class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length= 100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
