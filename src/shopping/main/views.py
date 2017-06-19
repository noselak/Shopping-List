from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import ShoppingList


class ShoppingListsView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    template_name = 'main/shopping_lists.html'
    context_object_name = 'shopping_lists'
    
    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class ShoppingListDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    template_name = 'main/shopping_list_detail.html'
    context_object_name = 'shopping_list'
    
    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class ShoppingListDeleteView(View):
    def post(self, request, pk):
        shopping_list = ShoppingList.objects.get(pk=pk)
        if shopping_list.user == self.request.user:
            shopping_list.delete()
        return redirect('main:shopping_lists_view')
