from rest_framework import serializers
from .models import Customers, Category_domains


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_domains
        fields = '__all__'

