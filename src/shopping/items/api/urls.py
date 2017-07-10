from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CategoryListAPIView.as_view(), 
            name="category_list_api_view"),
    url(r'^(?P<pk>\d+)/items$', views.ItemsListAPIView.as_view(), 
            name='items_list_api_view'),
]