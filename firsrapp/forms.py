from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subjects = forms.CharField(label='Тема почты', widget=forms.TextInput(attrs={"class": "form-control", "autofocus": None}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={"class": "form-control"}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control", "autofocus": None}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegistration(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control", "autofocus": None}))
    email = forms.EmailField(label='Адрес', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category', 'is_published']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control"})
        }

