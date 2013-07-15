from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scouter.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)

urlpatterns += patterns('website.views',
    url(r'^$', 'homepage'),
    url(r'^oauth2callback/$', 'callback'),
    url(r'^auth_return/$', 'auth_return'),
    url(r'^clear_contacts/$', 'clear_contacts'),
    url(r'^mirror/subscription/reply/$', 'subscription_reply'),
)