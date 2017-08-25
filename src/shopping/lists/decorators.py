from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import ShoppingList, ShoppingItem

def user_is_list_owner(function):
    def wrap(self, request, *args, **kwargs):
        shopping_list = get_object_or_404(ShoppingList, pk=kwargs['pk'])
        if request.user == shopping_list.user:
            return function(self, request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    
    return wrap

def user_is_list_owner_via_item(function):
    def wrap(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            shopping_item = get_object_or_404(ShoppingItem, pk=kwargs['pk'])
        elif 'pk' in request.POST:
            pk = int(request.POST.get('pk'))
            shopping_item = get_object_or_404(ShoppingItem, pk=pk)
        else:
            raise ValueError('No shopping item found')
        
        shopping_list = shopping_item.shopping_list
        if request.user == shopping_list.user:
            return function(self, request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    
    return wrap