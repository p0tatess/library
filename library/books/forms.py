from django import forms
from django.contrib.auth.models import User
from .models import booksModel


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class booksForm(forms.ModelForm):
    class Meta:
        model = booksModel
        fields = ('book','data','days')




class turnBooks(forms.Form):

    # choice_book = forms.ChoiceField()

    choice_book = forms.CharField(label='Название книги')

