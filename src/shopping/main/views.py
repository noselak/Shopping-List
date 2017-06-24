from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class MainPageView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def get(self, request):
        template = 'main/main.html'
        context = {}
        return render(request, template, context)