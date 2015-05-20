from django.conf.urls import patterns, url
from birds import views

urlpatterns = patterns('',
    url(r'^login$', views.bird_login, name='user_login'),
    url(r'^logout$', views.bird_logout, name='user_logout'),
    url(r'^register$', views.bird_register, name='user_register'),
)