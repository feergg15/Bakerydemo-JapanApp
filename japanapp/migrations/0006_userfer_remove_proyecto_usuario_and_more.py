# Generated by Django 4.2.6 on 2024-03-06 18:57

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('japanapp', '0005_proyecto_img_alter_proyecto_modelo_filtro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, null=True, region='ES', unique=True)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='img')),
                ('groups', models.ManyToManyField(blank=True, related_name='userfers_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='userfers_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='modelo_filtro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Modelo_filtro', to='japanapp.filtro'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='modelo_suspes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Modelo_suspension', to='japanapp.suspension'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
