"""The MIT License

Copyright (c) 2009 Rodolfo da Silva Carvalho <rodolfo@rcarvalho.eti.br>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
