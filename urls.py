from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from registration import *
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('profile.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
