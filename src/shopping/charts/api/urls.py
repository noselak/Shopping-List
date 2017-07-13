from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShoppingItemsCountsAPIView.as_view(),
            name="shopping_items_counts_api_view"),
]