from django.db import models

# Create your models here.


class Branch(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]
    branch_name = models.CharField(max_length=100, help_text="Ingrese el Nombre de la Sucursal")
    address = models.CharField(max_length=100, help_text="Ingrese la Direccion del Gerente")
    phone = models.CharField(max_length=12, help_text="Ingrese el Telefono del Gerente")
    email = models.EmailField(max_length=100, help_text="Ingrese el Correo del Gerente")
    name = models.CharField(max_length=100, help_text="Ingrese el Nombre del Gerente")
    opening_date = models.DateField(max_length=100, help_text="Ingrese la Fecha de Trabajo")
    status = models.CharField(
        max_length=8, 
        choices=STATUS_CHOICES, 
        default='ACTIVE',
        help_text="Ingrese el Estado del Gerente"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branchs"