# Generated by Django 4.1.7 on 2023-03-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default='null', max_length=250, verbose_name='Contenido'),
        ),
    ]