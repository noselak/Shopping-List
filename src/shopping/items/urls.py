from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search-items/$', views.SearchItemsView.as_view(), name="search_items_view"),
]