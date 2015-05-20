from django.conf.urls import patterns, url

from pips_messages import views

urlpatterns = patterns('',
    url(r'^$', views.pip_listing, name='pip_listing'),
    url(r'^(\d+)/$', views.pip_details, name='pip_details'),
    url(r'^pip_add_likes/(\d+)$', views.pip_add_likes,
		name='pip.likes'),  
)