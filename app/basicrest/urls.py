# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import *

admin.site.site_header = 'Pets Example'

urlpatterns = patterns('',
    url(r'^pet/list$', PetListView.as_view()),
    url(r'^pet$', PetView.as_view()),
    url(r'^pet/(?P<id>.+)/$', PetView.as_view()),
    url(r'^pet/(?P<id>.+)/activity$', PetActivityView.as_view())
)
