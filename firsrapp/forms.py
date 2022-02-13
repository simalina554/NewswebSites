from django import forms
from .models import *


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

    # title = forms.CharField(max_length=200, label='Название новости',
    #                         widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Текст', required=False,
    #                           widget=forms.Textarea(attrs={"class": "form-control"}))
    # photo = forms.ImageField(widget=forms.Textarea(attrs={"class": "form-control"}))
    # is_published = forms.BooleanField(label='Опубликовано?')
    # category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(),
    #                                   widget=forms.Select(attrs={"class": "form-control"}))

