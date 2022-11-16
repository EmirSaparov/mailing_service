from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SubscribedUsersForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Имя')
    last_name = forms.CharField(max_length=20, help_text='Фамилия')
    birth_date = forms.DateField(required=True, help_text='Дата рождения')
    email = forms.EmailField(required=True, help_text='Адрес электронной почты')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

