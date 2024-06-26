from django.db import models

class Car(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    ano = models.IntegerField(verbose_name='Ano')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
