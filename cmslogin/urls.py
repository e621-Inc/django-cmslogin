from __future__ import unicode_literals

from django.conf.urls import url

from .views import LoginView, LogoutView


urlpatterns = [
    url(
        r'^login/$',
        LoginView.as_view(),
        name='cmslogin-login'
    ),
    url(
        r'^logout/$',
        LogoutView.as_view(),
        name='cmslogin-logout'
    ),
]
