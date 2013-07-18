from django.conf.urls import patterns, include, url
from messages.views import index, topic
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MessageBoard.views.home', name='home'),
    # url(r'^MessageBoard/', include('MessageBoard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="index"),
    url(r'^topic/(?P<topic_id>\d+)/$', topic, name="topic"),
    
)
