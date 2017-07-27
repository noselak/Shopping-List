from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm
)
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
                               label="Username", max_length=30,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter Your Name',
                                    'class': 'form-control login-field',
                                    'name': 'username'
                                    })
                               )
    password = forms.CharField(
                               label="Password",
                               max_length=30,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'form-control login-field',
                                    'name': 'password',
                                    'type': 'password'
                                    })
                               )


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
    
    username = forms.CharField(
                               label="Username", max_length=30,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter Your Name',
                                    'class': 'form-control login-field',
                                    'name': 'username'
                                    })
                               )
    password1 = forms.CharField(
                               label="Password",
                               max_length=30,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'form-control login-field',
                                    'name': 'password1',
                                    'type': 'password'
                                    })
                               )
    password2 = forms.CharField(
                               label="Confirm Password",
                               max_length=30,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'Confirm Password',
                                    'class': 'form-control login-field',
                                    'name': 'password2',
                                    'type': 'password'
                                    })
                               )
    email = forms.EmailField(
                               label="E-mail", max_length=30,
                               widget=forms.TextInput(attrs={
                                    'placeholder': 'E-mail',
                                    'class': 'form-control login-field',
                                    'name': 'username'
                                    })
                               )
                               
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email) \
                                 .exclude(username=username).exists():
            raise forms.ValidationError(u'This e-mail already exists in the database')
        return email


class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(
                                   label="Password",
                                   max_length=30,
                                   widget=forms.TextInput(attrs={
                                        'placeholder': 'Old Password',
                                        'class': 'form-control login-field',
                                        'type': 'password'
                                        })
                                   )
    new_password1 = forms.CharField(
                                   label="Password",
                                   max_length=30,
                                   widget=forms.TextInput(attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control login-field',
                                        'type': 'password'
                                        })
                                   )
    new_password2 = forms.CharField(
                                   label="Confirm Password",
                                   max_length=30,
                                   widget=forms.TextInput(attrs={
                                        'placeholder': 'Confirm Password',
                                        'class': 'form-control login-field',
                                        'type': 'password'
                                        })
                                    )
