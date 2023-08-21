from django.shortcuts import render
from rest_framework import viewsets
from .models import Customers, Category_domains
from .serializer import EmployeeSerializer, CategorySerializer
from rest_framework import permissions
# Create your views here.



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = EmployeeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category_domains.objects.all()
    serializer_class = CategorySerializer