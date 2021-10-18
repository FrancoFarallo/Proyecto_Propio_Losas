from django.db import models

# Create your models here.


class Losa (models.Model):
    Largo = models.CharField(max_length=8)
    Ancho = models.CharField(max_length=8)


    def LosaX (self):
        cadena= "{0}, {1}"
        return cadena.format(self.Ancho, self.Largo)


    def __str__(self):
        return self.LosaX ()