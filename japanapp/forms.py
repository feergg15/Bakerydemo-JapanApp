from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    pass

class RegisterForm(UserCreationForm):

    avatar = forms.ImageField(required=False)

    email = forms.EmailField()

    class Meta:
        model=Userfer
        fields = ['username','email','password1','password2','telefono','avatar']

class UserEditForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = Userfer
        fields = ['username','email','telefono','avatar']


class Proyecto(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ('modelo_coche', 'modelo_escape','modelo_llanta','modelo_volante','modelo_bk')