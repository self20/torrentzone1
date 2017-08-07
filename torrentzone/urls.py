from django.conf.urls import  url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^create/', views.create, name="create"),
    url(r'^delete_torrent/(?P<pk>\d+)/$', views.delete_torrent, name='delete_torrent'),
]
