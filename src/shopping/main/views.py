from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from .models import ShoppingList, ShoppingItem


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
    @method_decorator(login_required(login_url='users:login_view'))
    def post(self, request, pk):
        shopping_list = ShoppingList.objects.get(pk=pk)
        if shopping_list.user == self.request.user:
            shopping_list.delete()
        return redirect('main:shopping_lists_view')
        
        
class MarkShoppingItemView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def post(self, request):
        item_pk = int(request.POST.get('pk'))
        shopping_item = ShoppingItem.objects.get(pk=item_pk)
        
        if shopping_item.shopping_list.user == request.user:
            if shopping_item.bought is False:
                shopping_item.bought = True
            else:
                shopping_item.bought = False
            shopping_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))