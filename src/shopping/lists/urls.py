from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ShoppingListDetailView.as_view(),
            name='shopping_list_detail_view'),
    url(r'^(?P<pk>\d+)/delete/$', views.ShoppingListDeleteView.as_view(),
            name='shopping_list_delete_view'),
    url(r'^(?P<pk>\d+)/edit/$', views.EditShoppingListView.as_view(),
            name='edit_shopping_list_view'),
    url(r'^(?P<pk>\d+)/archive/$', views.ArchiveShoppingListView.as_view(),
            name='archive_shopping_list_view'),
    url(r'^(?P<pk>\d+)/add-items/$', views.AddItemsToListView.as_view(),
            name='add_items_to_list_view'),
    url(r'^(?P<pk>\d+)/delete-items/$', views.DeleteItemsFromListView.as_view(),
            name='delete_items_from_list_view'),
    url(r'^edit-items/$', views.EditItemsView.as_view(),
            name='edit_items_view'),
    url(r'^add/$', views.AddShoppingListView.as_view(),
            name="add_shopping_list_view"),
    url(r'^mark-items/$', views.MarkShoppingItemView.as_view(),
            name="mark_shopping_item_view"),
    url(r'^archive/$', views.ShoppingListsArchiveView.as_view(),
            name="shopping_lists_archive_view"),
    url(r'^search/$', views.ShoppingListsSearchView.as_view(),
            name='shopping_lists_search_view'),
    url(r'^$', views.ShoppingListsView.as_view(),
            name='shopping_lists_view'),
]