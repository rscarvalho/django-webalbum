from django.conf.urls.defaults import *
from webalbum.views import fit

urlpatterns = patterns('',
    url(r'^crop/(?P<id>\d+)/(?:(?P<width>\d+),(?P<height>\d+)/)?$', fit, name="crop-photo"),
)
