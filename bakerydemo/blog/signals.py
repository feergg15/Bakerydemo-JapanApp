import os
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import Group , User
from django.dispatch import receiver
from django.core.mail import BadHeaderError,send_mail

def write_email_to_file(subject, message):
    file_path = '/home/fernando/Escritorio/TRABAJOS_2ASIR/bakerydemo/bakerydemo/blog/mail.txt'
    with open(file_path, 'a') as f:
        f.write(f'Subject: {subject}\n')
        f.write(f'Message: {message}\n\n')

@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    try:
        grupo = Group.objects.get(name='Blogger')
        usuario = User.objects.get(username=user)
        correo = User.objects.get(username=user).email
    except:
         print(f"ERROR")

    if not grupo in usuario.groups.all():
        usuario.groups.add(grupo.id)
        usuario.save()
        if user.last_login is None:
            subject = 'Nuevo usuario registrado'
            message = f'Bienvenido, {user.username}! Has sido añadido al grupo blogger en la web Japan-Tuner.'
            write_email_to_file(subject, message)
    else:
        print(f"El usuario, {usuario.username}, ya se encuentra al grupo {grupo.name}.")
