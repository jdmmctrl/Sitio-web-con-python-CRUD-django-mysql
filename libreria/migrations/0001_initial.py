# Generated by Django 4.2.2 on 2023-06-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='descripcion')),
            ],
        ),
    ]
