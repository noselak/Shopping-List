from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login_view'),
    url(r'^register/$', views.RegisterView.as_view(), name='register_view'),
    url(r"^logout/$", auth_views.logout_then_login, name="logout_view"),
]