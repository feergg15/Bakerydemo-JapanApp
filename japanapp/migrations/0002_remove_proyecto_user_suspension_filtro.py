# Generated by Django 4.2.6 on 2023-11-08 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('japanapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='user',
        ),
        migrations.CreateModel(
            name='Suspension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20, null=True)),
                ('modelo_suspes', models.CharField(max_length=20, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='foto')),
                ('modelo_coche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='japanapp.coche')),
            ],
        ),
        migrations.CreateModel(
            name='Filtro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20, null=True)),
                ('modelo_filtro', models.CharField(max_length=20, null=True)),
                ('material', models.CharField(max_length=20, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='foto')),
                ('modelo_coche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='japanapp.coche')),
            ],
        ),
    ]
