from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import filter_by_time_period, get_ordered_data


class ShoppingItemsCountsAPIView(APIView):
    def get(self, request):
        time_period = request.GET.get('time-period')

        # Checking for time period. If true: returning queryset filtered by 
        # date and user.
        if time_period:
            shopping_lists = filter_by_time_period(self.request, time_period)
        else:
            shopping_lists = ShoppingList.objects \
                .filter(user=self.request.user)

        # Getting ordered dictionary with shopping item names and quantities.
        # Ordered by quantity descending
        ordered_data = get_ordered_data(shopping_lists)

        # Creating lists of item's labels and values. Returns 10 most
        # popular items.
        labels = [key for key in ordered_data.keys()][:10]
        values = [value for value in ordered_data.values()][:10]

        response = {
            'labels': labels,
            'values': values
        }

        return Response(response)
