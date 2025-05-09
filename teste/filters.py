from django_filters import rest_framework as filters
from teste import models

class ClientFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    
    class Meta:
        model = models.Client
        fields = ['id']


class EmployeeFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    
    class Meta:
        model = models.Employee
        fields = ['id', 'name']
        

class SaleFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    client_id = filters.NumberFilter(field_name='client_id', lookup_expr='exact')
    product_id = filters.NumberFilter(field_name='product_id', lookup_expr='exact')
    
    class Meta:
        model = models.Sale
        fields = ['id', 'client_id', 'product_id']
        

class ProductFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    quantity = filters.NumberFilter(field_name='quantity', lookup_expr='exact')
   
    class Meta:
        model = models.Product
        fields = ['id', 'description', 'quantity']