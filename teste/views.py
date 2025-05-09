from django.shortcuts import render
from rest_framework import viewsets, permissions
from teste import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from teste import models, serializers, filters
from teste.pagination import CustomLimitOffsetPagination

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ClientFilter
    pagination_class = CustomLimitOffsetPagination 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ProductFilter
    pagination_class = CustomLimitOffsetPagination 
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.EmployeeFilter
    pagination_class = CustomLimitOffsetPagination 
    
class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.SaleFilter
    pagination_class = CustomLimitOffsetPagination 