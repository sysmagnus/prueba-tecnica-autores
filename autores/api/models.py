from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    bio = models.CharField(max_length=256, null=True)


class Libro(models.Model):
    title = models.CharField(max_length=256, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True, null=True)
    resumen = models.TextField(null=True, blank=True)