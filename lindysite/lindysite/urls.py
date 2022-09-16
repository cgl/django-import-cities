from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Examples:
    # url(r'^$', 'lindysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path(r'^admin/', admin.site.urls),
    url(r'', include('plus.urls')),
]
