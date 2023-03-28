from django.db import models

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")
    phone = models.IntegerField(  verbose_name="Telefono")
    email = models.EmailField(verbose_name="Imagen")
    message = models.TextField(default='null', verbose_name="Mensaje")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado" )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.name}"