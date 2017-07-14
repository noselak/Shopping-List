import datetime
from dateutil import relativedelta
from collections import OrderedDict

from django.db.models import Sum

from lists.models import ShoppingList, ShoppingItem

def filter_by_time_period(request, time_period):
    today = datetime.datetime.today()
    previous_date = None
    if time_period == 'last-month':
        previous_date = today + relativedelta.relativedelta(months=-1)
    elif time_period == 'last-year':
        previous_date = today + relativedelta.relativedelta(years=-1)
    shopping_lists = ShoppingList.objects \
        .filter(user=request.user) \
        .filter(date__range=[previous_date, today])
    return shopping_lists

def get_ordered_data(shopping_lists):
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

    ordered_data = OrderedDict(sorted(item_quantities.items(),
                               key=lambda t: t[1], reverse=True))
    return ordered_data