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

from webalbum.models import Album, Picture
from django import template
from django.core.urlresolvers import reverse
from django.conf import settings
from webalbum import settings as album_settings

register = template.Library()

@register.simple_tag
def album_thumbnail(id):
    album = Album.objects.get(pk=id)
    img_str = "<img src='%s' width='150' height='150' alt='%s' title='%s'/>"
    #img_url = reverse("crop-photo", kwargs=dict(id=album.image.id, width=80,
    #                                            height=80))
    img_url = album.image.url
    
    return img_str % (img_url, album.name, album.name)
    
@register.simple_tag
def pic_thumbnail(picture, width=225, height=150):
    return picture.thumbnail


class PicturePaginatorNode(template.Node):
    def render(self, context):
        if context.has_key("picture_error"):
            return ""
        
        page = context['picture_page']
        paginator = context['picture_paginator']
        album = context['album']
        
        if paginator.num_pages == 1:
            return ""
        
        html = "<div class='paginator span-19 last'><ul>\n"
        if page.has_previous():
            html += "<li><a href='?album=%d&picture_page=%d'>%s</a></li>\n" % \
                                                    (album.id, page.next_page_number(),
                                                     album_settings.PICT_PAGE_PREV)
        
        for page_number in paginator.page_range:
            if page.number == page_number:
                html += "<li class='current'>"
                page_content = u"%(page)d"
            else:
                html += "<li>"
                page_content = u"<a href='?album=%(album)d&picture_page=%(page)d'>%(page)d</a>"
            html += page_content % {'album': album.id, 'page': page_number}
            html += "</li>\n"
        
        if page.has_next():
            html += "<li><a href='?album=%d&picture_page=%d'>%s</a></li>\n" % \
                                                    (album.id, page.next_page_number(),
                                                     album_settings.PICT_PAGE_NEXT)
        
        html += "</ul></div>"
        return html

@register.tag
def picture_paginator(parser, token):
    return PicturePaginatorNode()

class AlbumsPaginatorNode(template.Node):
    def render(self, context):
        if context.has_key("album_error"):
            return ""
        page = context['album_page']
        paginator = context['album_paginator']
        
        if paginator.num_pages == 1:
            return ""
        
        html = "<div class='paginator span-14'><ul>\n"
        if page.has_previous():
            html += "<li><a href='?album_page=%d'>%s</a></li>\n" % \
                                                    (page.previous_page_number(),
                                                     album_settings.ALBUM_PAGE_PREV)
        else:
            html += "<li>" + album_settings.ALBUM_PAGE_NO_PREV + "</li>"
        
        for page_number in paginator.page_range:
            html += "<li>"
            if page.number == page_number:
                page_content = "%(page)d"
            else:
                page_content = "<a href='?album_page=%(page)d'>%(page)d</a>"
            html += page_content % {'page': page_number}
            html += "</li>\n"
        
        if page.has_next():
            html += "<li><a href='?album_page=%d'>%s</a></li>\n" % \
                                                    (page.next_page_number(),
                                                     album_settings.ALBUM_PAGE_NEXT)
        else:
            html += "<li>" + album_settings.ALBUM_PAGE_NO_NEXT + "</li>"
        
        html += "</ul></div>"
        return html

@register.tag
def album_paginator(parser, token):
    return AlbumsPaginatorNode()
