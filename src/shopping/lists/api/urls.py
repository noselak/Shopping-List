from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ShoppingListDetailAPIView.as_view(), name='shopping_list_detail_api_view'),
    url(r'^$', views.ShoppingListsAPIView.as_view(), 
            name="shopping_lists_api_view"),
]