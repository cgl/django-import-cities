from django.conf.urls import url
from plus import views

urlpatterns = [
    url(r'^$', views.events_list, name='events_list'),
    url(r'^cities$', views.events_list, name='cities_list'),
]
