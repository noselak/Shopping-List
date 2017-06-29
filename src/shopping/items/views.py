from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from lists.models import ShoppingList

from .models import Item


class SearchItemsView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def get(self, request):
        shopping_list_pk = request.GET.get('shopping_list_pk')
        query = request.GET.get('q')
        template = 'items/search_items.html'
        items = None
        
        # deliver queryset after typing at least 3 characters
        if len(query) > 2:
            items = Item.objects.filter(name__icontains=query)
            
        context = {
            'items': items,
            'shopping_list_pk': shopping_list_pk,
        }
            
        return render(request, template, context)
