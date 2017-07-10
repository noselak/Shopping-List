from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
    )

from lists.models import ShoppingList, ShoppingItem


class ShoppingListsSerializer(ModelSerializer):
    list_detail_url = HyperlinkedIdentityField(
        view_name='lists_api:shopping_list_detail_api_view',
        lookup_field='pk'
        )
    
    class Meta:
        model = ShoppingList
        fields = ('name', 'pk', 'shop', 'date', 'timestamp', 'list_detail_url')


class ShoppingListCreateSerializer(ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('name', 'shop', 'date')


class ShoppingListDetailSerializer(ModelSerializer):
    shopping_items = SerializerMethodField()

    class Meta:
        model = ShoppingList
        fields = ('name', 'shop', 'date', 'timestamp', 'shopping_items')

    def get_shopping_items(self, obj):
        shopping_list = ShoppingList.objects.get(pk=obj.pk)
        shopping_items = shopping_list.shoppingitem_set.all()
        return ShoppingItemSerializer(shopping_items, many=True).data


class ShoppingItemSerializer(ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ('name', 'item', 'quantity', 'bought')