from rest_framework.generics import ListAPIView, RetrieveAPIView

from lists.models import ShoppingList, ShoppingItem

from .serializers import ShoppingListsSerializer, ShoppingListDetailSerializer


class ShoppingListsAPIView(ListAPIView):
    serializer_class = ShoppingListsSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = ShoppingList.objects.filter(user=self.request.user)
        return qs


class ShoppingListDetailAPIView(RetrieveAPIView):
    serializer_class = ShoppingListDetailSerializer

    def get_queryset(self, *args, **kwargs):
        qs = ShoppingList.objects.filter(user=self.request.user)
        return qs