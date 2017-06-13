from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShoppingListsView.as_view(), name='shopping_lists_view'),
]