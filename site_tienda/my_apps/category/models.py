from django.db import models

class Category(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]
    category_name = models.CharField(max_length=100, help_text="Ingrese el Nombre de la Categoria del producto")
    description = models.TextField(help_text="Ingrese la Descripcion del producto")
    status = models.CharField(
        max_length=8, 
        choices=STATUS_CHOICES, 
        default='ACTIVE',
        help_text="Ingrese el Estado del Gerente"
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categorys"
