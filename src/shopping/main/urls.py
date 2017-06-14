from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ShoppingListDetailView.as_view(), name='shopping_list_detail_view'),
    url(r'^$', views.ShoppingListsView.as_view(), name='shopping_lists_view'),
]