from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ItemDetailAPIView.as_view(), 
            name='item_detail_api_view'),
    url(r'^add/$', views.CreateItemAPIView.as_view(), 
            name="create_item_api_view"),
    url(r'^categories/(?P<pk>\d+)/$', views.ItemsListAPIView.as_view(), 
            name='items_list_api_view'),
    url(r'^categories/$', views.CategoryListAPIView.as_view(), 
            name="category_list_api_view"),
]