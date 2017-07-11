from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView
    )

from lists.models import ShoppingList, ShoppingItem

from .serializers import (
    ShoppingListsSerializer,
    ShoppingListDetailSerializer,
    ShoppingListCreateSerializer,
    ShoppingItemSerializer,
    CreateShoppingItemSerializer
    )
from .permissions import IsOwner


class ShoppingListsAPIView(ListAPIView):
    serializer_class = ShoppingListsSerializer

    def get_queryset(self, *args, **kwargs):
        qs = ShoppingList.objects.filter(user=self.request.user)
        return qs


class AddShoppingListAPIView(CreateAPIView):
    serializer_class = ShoppingListCreateSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = ShoppingList.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ShoppingListDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListDetailSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self, *args, **kwargs):
        qs = ShoppingList.objects.all()
        return qs


class ShoppingItemsAPIView(ListAPIView):
    serializer_class = ShoppingItemSerializer
    
    def get_queryset(self, *args, **kwargs):
        shopping_list = ShoppingList.objects.filter(user=self.request.user) \
                                            .get(pk=self.kwargs.get('pk'))
        qs = shopping_list.shoppingitem_set.all()
        return qs


class AddShoppingItemAPIView(CreateAPIView):
    serializer_class = CreateShoppingItemSerializer
