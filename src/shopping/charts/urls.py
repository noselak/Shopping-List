from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BoughtItemsChartView.as_view(),
            name="bought_items_chart_view"),
]