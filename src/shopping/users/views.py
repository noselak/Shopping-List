from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import LoginForm


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
                    return redirect('main:shopping_lists_view')
                else:
                    messages.error(request, 
                                'User {} has been blocked'.format(username), 
                                extra_tags='login')
                    return redirect('users:login_view')
            else:
                messages.error(request, 'Wrong password and/or username', 
                                extra_tags='login')
                return redirect('users:login_view')
