from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    url('^admin/', include(admin.site.urls)),
    url('^basicrest/', include('app.basicrest.urls')),
)
