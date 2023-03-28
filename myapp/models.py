from django.db import models

# Create your models here.

class Subscription(models.Model):

    email = models.EmailField(verbose_name="Imagen")

    class Meta:
        verbose_name = "Correo"
        verbose_name_plural = "Correos"

    def __str__(self):
        return f"{self.email}"