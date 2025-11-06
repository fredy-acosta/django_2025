from django.db import models

class Tax(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]
    tax_name = models.CharField(max_length=100, help_text="Ingrese el IVA Porcentual")
    tax_percentege = models.CharField(max_length=12, help_text="Ingrese el IVA a Cobrar")
    description = models.TextField(help_text="Ingrese la Descripcion del IVA")
    status = models.CharField(
        max_length=8, 
        choices=STATUS_CHOICES, 
        default='ACTIVE',
        help_text="Ingrese el Estado del Gerente"
    )

    def __str__(self):
        return self.tax_name

    class Meta:
        verbose_name = "tax"
        verbose_name_plural = "taxs"
