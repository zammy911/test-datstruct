from django.conf.urls.defaults import * 
from django.contrib import admin
from django.conf import settings
import registration

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('profile.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
