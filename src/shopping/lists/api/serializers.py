from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lists.models import ShoppingList, ShoppingItem


class ShoppingListsSerializer(ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('name', 'pk', 'shop', 'date', 'timestamp')


class ShoppingListDetailSerializer(ModelSerializer):
    shopping_items = SerializerMethodField()

    class Meta:
        model = ShoppingList
        fields = ('name', 'shop', 'date', 'timestamp', 'shopping_items')

    def get_shopping_items(self, obj):
        shopping_list = ShoppingList.objects.get(pk=obj.pk)
        shopping_items = shopping_list.shoppingitem_set.all()
        return ShoppingItemDetailSerializer(shopping_items, many=True).data


class ShoppingItemDetailSerializer(ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ('name', 'item', 'quantity', 'bought')