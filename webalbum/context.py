from django.core.paginator import Paginator, InvalidPage
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from webalbum import settings as album_settings
from django.http import Http404
from webalbum.models import Album

def get_album_list(request, context):
    try:
        page = int(request.GET.get("album_page", 1))
    except ValueError:
        context['album_error'] = _("The page is invalid.")
        return
    
    albums = Album.objects.order_by("-pub_date")
    if request.GET.has_key("album_search"):
        albums = albums.filter(name__icontains=request.GET['album_search'])
    paginator = Paginator(albums, album_settings.ALBUMS_PER_PAGE)
    
    try:
        ppage = paginator.page(page)
    except InvalidPage:
        context['album_error'] = _("The page is invalid.")
        return
    
    context['album_page'] = ppage
    context['album_set'] = ppage.object_list
    context['album_paginator'] = paginator


def load_album(request, context):
    try:
        album = Album.objects.get(pk=request.GET.get("album", 0))
    except Album.DoesNotExist:
        if Album.objects.count() > 0:
            album = Album.objects.order_by("-pub_date")[0]
        else:
            raise Http404
    
    try:
        page = int(request.GET.get("picture_page", 1))
    except ValueError:
        raise Http404
    
    paginator = Paginator(album.picture_set.all(), album_settings.PHOTOS_PER_PAGE)
    try:
        ppage = paginator.page(page)
    except InvalidPage:
        raise Http404
        
    context['album'] = album
    
    context['picture_set'] = ppage.object_list
    context['picture_page'] = ppage
    context['picture_paginator'] = paginator
