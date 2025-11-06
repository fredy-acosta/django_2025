from django.db import models
from my_apps.category.models import Category
from my_apps.tax.models import Tax
# Create your models here.



class Product(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    product_code = models.CharField(max_length=20, help_text="Ingrese el Codigo del Producto")
    product_name = models.CharField(max_length=100, help_text="Ingrese el Nombre del Producto")
    description = models.TextField(help_text="Ingrese la Descripcion del producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ingrese el Precio del Producto")
    weinght = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ingrese el Peso del Producto")
    dimentions = models.CharField(max_length=100, help_text="Ingrese el Tamaño del Producto")
    brand = models.CharField(max_length=100, help_text="Ingrese la Marca del Producto")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el Tipo de Producto"
    )
    tax = models.ForeignKey(
        Tax, 
        on_delete=models.CASCADE, 
        help_text="Seleccione el Tipo de Impuesto"
    )
    status = models.CharField(
        max_length=8, 
        choices=STATUS_CHOICES, 
        default='ACTIVE',
        help_text="Ingrese el Estado del Producto"
    )

    def __str__(self):
        return f"{self.product_name} - {self.brand}"

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"