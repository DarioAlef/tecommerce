from rest_framework import serializers
from teste import models

class ClientSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    name= serializers.CharField(max_length=70)
    age = serializers.IntegerField(min_value=0, max_value=100)
    cpf = serializers.CharField(max_length=12)
    
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'age', 'cpf', 'active', 'modified_at']  
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'description', 'quantity', 'active', 'modified_at']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'registration', 'active', 'modified_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'active', 'modified_at']
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'title', 'author', 'active', 'modified_at']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'client', 'employee', 'product', 'nrf', 'modified_at']        