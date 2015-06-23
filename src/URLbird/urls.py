"""URLbird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from account import views as account_views
from .settings import *
from shorturls.views import LinkCreate, LinkShow, RedirectToLongURL
from api import views

router = routers.DefaultRouter()
router.register(r'account', views.BookmarkViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', account_views.AddUserView.as_view(), name="register"),
    # url(r'^$', views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^create$', LinkCreate.as_view(), name='home'),
    url(r'^link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'),
    url(r'^r/(?P<short_url>\w+)$', RedirectToLongURL.as_view(), name='redirect_short_url'),
    url(r'^user/(?P<user_id>\d+)$', account_views.UserDetailView.as_view(), name="user_data"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),


]
if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)