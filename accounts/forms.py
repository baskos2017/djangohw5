from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Введіть пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Підтвердіть пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Ім\'я користувача',
            'email': 'Електронна пошта',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Паролі не співпадають.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Ім\'я')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')