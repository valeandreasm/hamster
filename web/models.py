from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 40)
    correo = models.CharField(max_length = 40)
    
    def __str__(self) ->str:
        return f'{self.nombre}, {self.correo}'