from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ShoppingListDetailAPIView.as_view(), 
            name='shopping_list_detail_api_view'),
    url(r'^(?P<pk>\d+)/items$', views.ShoppingItemsAPIView.as_view(), 
            name='shopping_items_api_view'),
    url(r'^add/$', views.AddShoppingListAPIView.as_view(), 
            name="add_shopping_list_api_view"),
    url(r'^add-item/$', views.AddShoppingItemAPIView.as_view(), 
            name="add_shopping_item_api_view"),
    url(r'^$', views.ShoppingListsAPIView.as_view(), 
            name="shopping_lists_api_view"),
]