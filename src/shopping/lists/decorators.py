from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import ShoppingList

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