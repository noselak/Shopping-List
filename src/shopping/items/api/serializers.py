from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
    )

from items.models import Item, Category


class CategorySerializer(ModelSerializer):
    items_url = HyperlinkedIdentityField(
        view_name='items_api:items_list_api_view',
        lookup_field='pk'
        )

    class Meta:
        model = Category
        fields = ('name', 'items_url')


class ItemsListSerializer(ModelSerializer):
    item_url = HyperlinkedIdentityField(
        view_name='items_api:item_detail_api_view',
        lookup_field='pk'
        )

    class Meta:
        model = Item
        fields = ('name', 'category', 'item_url')


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'category')