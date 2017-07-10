from rest_framework.generics import (
    ListAPIView,
    )

from items.models import Category, Item

from .serializers import CategorySerializer, ItemsSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = Category.objects.all()
        return qs


class ItemsListAPIView(ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs.get('pk'))
        qs = category.item_set.all()
        return qs