from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Service(models.Model):

    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", upload_to="service" ,verbose_name="Imagen")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado" )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return f"{self.title}"