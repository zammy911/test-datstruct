from django.conf.urls.defaults import *
from profile.views import *

urlpatterns = patterns('',
    url(r'^$', show_contact, name="show_contact"),
)

