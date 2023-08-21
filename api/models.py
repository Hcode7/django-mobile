from django.db import models

# Create your models here.

class Category_domains(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Customers(models.Model):
    full_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category_domains, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
