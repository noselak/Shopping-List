from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm, PasswordChangeCustomForm


class LoginView(View):
    template = 'users/login.html'

    def get(self, request):
        login_form = LoginForm(None)
        context = {
            'login_form': login_form,
        }
        return render(request, self.template, context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:main_page_view')
                else:
                    messages.error(request,
                                   'User {} has been blocked'.format(username),
                                   extra_tags='login')
            else:
                messages.error(request, 'Incorrect password and/or username',
                               extra_tags='login')
        context = {
            'login_form': login_form,
        }
        return render(request, self.template, context)


class RegisterView(View):
    template = 'users/register.html'

    def get(self, request):
        register_form = RegisterForm(None)
        context = {
            'register_form': register_form,
        }
        return render(request, self.template, context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            email = register_form.cleaned_data['email']
            user = register_form.save(commit=False)
            user.email = email
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:main_page_view')

        context = {
            'register_form': register_form,
        }
        return render(request, self.template, context)


class ChangePasswordView(View):
    template = 'users/password_change.html'

    def get(self, request):
        password_change_form = PasswordChangeCustomForm(None)
        context = {
            'password_change_form': password_change_form,
        }
        return render(request, self.template, context)

    def post(self, request):
        password_change_form = PasswordChangeCustomForm(user=request.user,
                                                        data=request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password has been changed!',
                             extra_tags='password')
            return redirect('main:main_page_view')

        context = {
            'password_change_form': password_change_form
        }
        return render(request, self.template, context)
