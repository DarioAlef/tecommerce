from django.db import models
from django.db import models


class ModelBase(models.Model):
    abstract = True
    
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='is_active',
        null=False,
        default=True
    )
    


    class Meta:
        abstract = True
        managed = True
        

    
class Client(ModelBase):
    id = models.BigAutoField(
        auto_created=True,
        db_column='id',
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='name',
        max_length=70,
        null=False
    )
    age = models.IntegerField(
        db_column='age',
        null=False
    )
    cpf = models.CharField(
        db_column='cpf',
        max_length=12,
        null=False
    )
    # active = models.BooleanField(
    #     db_column='is_active',
    #     null=False,
    #     default=True
    # )
    # created_at = models.DateTimeField(
    #     db_column='created_at',
    #     auto_now_add=True,
    #     null=True
    # )
    # modified_at = models.DateTimeField(
    #     db_column='modified_at',
    #     auto_now=True,
    #     null=True
    # )


class Product(ModelBase):
    id = models.BigAutoField(
        db_column='id',
        auto_created=True,
        null=False,
        primary_key=True
    )
    description = models.CharField(
        db_column='tx_description',
        max_length=100,
        null=False
    )
    quantity = models.IntegerField(
        db_column='quantity',
        null=False
    )
    
class Employee(ModelBase):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
        auto_created=True
    )
    name = models.CharField(
        db_column='name',
        max_length=70,
        null=False
    )
    registration = models.CharField(
        db_column='registration',
        max_length=15,
        null=False
    )
    

class Sale(ModelBase):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
        auto_created=True
    )
    client = models.ForeignKey(
        Client,
        db_column='client_id',
        on_delete=models.CASCADE,
        null=False
    )
    employee = models.ForeignKey(
        Employee,
        db_column='employee_id',
        on_delete=models.CASCADE,
        null=False
    )
    product = models.ForeignKey(
        Product,
        db_column='product_id',
        on_delete=models.CASCADE,
        null=False
    )
    nrf = models.CharField(
        db_column='nrf',
        max_length=200,
        null=False
    )