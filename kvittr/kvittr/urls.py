from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('theme.urls')),
    url(r'^birds/', include('birds.urls')),
    url(r'^pips_messages/', include('pips_messages.urls')),
]
]
