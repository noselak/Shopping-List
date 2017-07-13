from collections import OrderedDict

from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response

from lists.models import ShoppingList, ShoppingItem


class ShoppingItemsCountsAPIView(APIView):
    def get(self, request):
        shopping_lists = ShoppingList.objects.filter(user=self.request.user)
        shopping_items = ShoppingItem.objects \
                                     .filter(shopping_list__in=shopping_lists) \
                                     .filter(bought=True)
        item_names = [name.get('name') for name in
                      shopping_items.values('name').distinct()]

        item_quantities = dict()

        for name in item_names:
            quantity = shopping_items.filter(name=name) \
                                     .aggregate(Sum('quantity')) \
                                     .get('quantity__sum')
            item_quantities[name] = quantity

        data = OrderedDict(sorted(item_quantities.items(),
                           key=lambda t: t[1], reverse=True))
        
        labels = [key for key in data.keys()]
        values = [value for value in data.values()]
        
        response = {
            'labels': labels,
            'values': values
        }

        return Response(response)
