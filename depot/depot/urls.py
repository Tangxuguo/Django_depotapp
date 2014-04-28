from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from depotapp.views import login_view,logout_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^depot/', include('depot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^accounts/login/$', login_view),
     (r'^accounts/logout/$', logout_view),
)

urlpatterns += patterns ('',
 (r'^depotapp/', include('depotapp.urls')),
 url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework')),
)

urlpatterns += staticfiles_urlpatterns()

