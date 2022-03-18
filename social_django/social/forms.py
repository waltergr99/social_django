from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Codigo del alumno' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username' ,'password1', 'email', 'password2']
        help_texts = {k: "" for k in fields}   
#Crear form apartir del modelo de mi BD 
class PostForm(forms.ModelForm):

    content = forms.CharField(label='' , widget=forms.Textarea(attrs={'rows':2, 'placeholder' : '¿Qué esta pasando?'}), required=True )

    class Meta:
        model = Post
        fields = ['content']