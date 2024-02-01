# Generated by Django 4.2.9 on 2024-02-01 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256, null=True)),
                ('email', models.CharField(max_length=256, null=True)),
                ('bio', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('fecha_publicacion', models.DateField(auto_now_add=True, null=True)),
                ('resumen', models.TextField(blank=True, null=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.autor')),
            ],
        ),
    ]
