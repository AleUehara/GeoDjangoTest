# Import django modules
from django.conf.urls.defaults import *


urlpatterns = patterns('waypoints.views',
    url(r'^$', 'index', name='waypoints-index'),
    url(r'^save$', 'save', name='waypoints-save'),
)
