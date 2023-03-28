from django.db import models
from ckeditor.fields import RichTextField 
from django.utils.text import slugify

# Create your models here.

class About(models.Model):

    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", upload_to="articles" ,verbose_name="Imagen")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado" )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Nosotro"
        verbose_name_plural = "Nosotros"

    def __str__(self):
        return f"{self.title}"
    
class Technologies(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el ")

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.name



class Team(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")
    profession = models.CharField(max_length=150, verbose_name="Profesión")
    description = RichTextField(verbose_name="Descripcion")
    photo = models.ImageField(default="null", upload_to="teams" ,verbose_name="Foto")
    technologies = models.ManyToManyField(Technologies, verbose_name="Tecnologias")
    url_facebook =  models.URLField(max_length=255, verbose_name="Facebook", null=True, blank=True )
    url_instagram = models.URLField(max_length=255, verbose_name="Instagram", null=True, blank=True)
    url_twitter = models.URLField(max_length=255,verbose_name="Twitter", null=True, blank=True)
    url_linkedin = models.URLField(max_length=255, verbose_name="Linkedin", null=True, blank=True)
    url_github = models.URLField(max_length=255, verbose_name="Githup", null=True, blank=True)
    url_portafolio = models.URLField(max_length=255, verbose_name="Portafolio")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado" )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return f"{self.name}"