"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^lists/', include('lists.urls', namespace="lists")),
    url(r'^items/', include('items.urls', namespace="items")),
    url(r'^charts/', include('charts.urls', namespace="charts")),
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls', namespace="main")),
    url(r'^api/lists/', include('lists.api.urls', namespace="lists_api")),
    url(r'^api/items/', include('items.api.urls', namespace="items_api")),
    url(r'^api/charts/', include('charts.api.urls', namespace="charts_api")),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)