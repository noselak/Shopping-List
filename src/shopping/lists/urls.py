from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ShoppingListDetailView.as_view(), name='shopping_list_detail_view'),
    url(r'^(?P<pk>\d+)/delete/$', views.ShoppingListDeleteView.as_view(), name='shopping_list_delete_view'),
    url(r'^add/$', views.AddShoppingListView.as_view(), name="add_shopping_list_view"),
    url(r'^list-items/$', views.MarkShoppingItemView.as_view(), name="mark_shopping_item_view"),
    url(r'^$', views.ShoppingListsView.as_view(), name='shopping_lists_view'),
]