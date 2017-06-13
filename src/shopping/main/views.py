from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ShoppingList


class ShoppingListsView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    template_name = 'main/shopping_lists.html'
    context_object_name = 'shopping_lists'
    
    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)

