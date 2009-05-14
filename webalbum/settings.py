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

from django.conf import settings

DEFAULT_EXTENSION = getattr(settings, "ALBUM_DEFAULT_EXTENSION", "jpg")
IMAGE_SIZE = getattr(settings, "ALBUM_IMAGE_SIZE", (480, 320))
IMAGE_WIDTH = IMAGE_SIZE[0]
IMAGE_HEIGHT = IMAGE_SIZE[1]
ALBUM_THUMBNAIL_SIZE = getattr(settings, "ALBUM_ALBUM_THUMBNAIL_SIZE", (180, 124))
PHOTO_THUMBNAIL_SIZE = getattr(settings, "ALBUM_PHOTO_THUMBNAIL_SIZE", (80, 80))

COVER_SIZE = getattr(settings, "ALBUM_COVER_SIZE", (150, 150))
COVER_THUMB_SIZE = getattr(settings, "ALBUM_COVER_THUMB_SIZE", None)
OVER_COVER = getattr(settings, "ALBUM_OVER_COVER", None)

PUT_WATERMARK = getattr(settings, "ALBUM_PUT_WATERMARK", False)

WATERMARK = getattr(settings, "ALBUM_WATERMARK", settings.MEDIA_ROOT + "images/watermark.png")

# Watermark position in final photograph
# Allowed values: bottomleft, bottomright, topleft, topright
WATERMARK_POSITION = getattr(settings, "ALBUM_WATERMARK_POSITION", "bottomleft")

WATERMARK_ALPHA = getattr(settings, "ALBUM_WATERMARK_ALPHA", 0.7)

# Crop Orientation
# Allowed values: center (others will be implemented soon)
CROP_ORIENTATION = getattr(settings, "ALBUM_CROP_ORIENTATION", "center")

ALBUMS_PER_PAGE = getattr(settings, "ALBUM_ALBUMS_PER_PAGE", 8)
PHOTOS_PER_PAGE = getattr(settings, "ALBUM_PHOTOS_PER_PAGE", 9)

PORTRAIT_SIZE = getattr(settings, "ALBUM_PORTRAIT_SIZE", False)

HAS_HIGHLIGHT = getattr(settings, "ALBUM_HAS_HIGHLIGHT", False)
HIGHLIGHT_SIZE = getattr(settings, "ALBUM_HIGHLIGHT_SIZE", (156, 314))
HIGHLIGHT_THUMB_SIZE = getattr(settings, "ALBUM_HIGHLIGHT_THUMB_SIZE", (240, 256))
HIGHLIGHT_WATERMARK = getattr(settings, "ALBUM_HIGHLIGHT_WATERMARK", None)
HIGHLIGHT_WATERMARK_POSITION = getattr(settings, "ALBUM_HIGHLIGHT_WATERMARK_POSITION",
                                          "bottomleft")
HAS_PHOTOGRAPHER = getattr(settings, "ALBUM_HAS_PHOTOGRAPHER", False)

ALBUM_PAGE_NEXT = getattr(settings, "ALBUM_PAGE_NEXT", "&raquo;")
ALBUM_PAGE_PREV = getattr(settings, "ALBUM_PAGE_PREV", "&laquo;")
ALBUM_PAGE_NO_NEXT = getattr(settings, "ALBUM_PAGE_NO_NEXT", "")
ALBUM_PAGE_NO_PREV = getattr(settings, "ALBUM_PAGE_NO_PREV", "")

PICT_PAGE_NEXT = getattr(settings, "ALBUM_PICTURE_PAGE_NEXT", "&raquo;")
PICT_PAGE_PREV = getattr(settings, "ALBUM_PICTURE_PAGE_PREV", "&laquo;")
