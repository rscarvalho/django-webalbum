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

from PIL import Image, ImageOps
from webalbum.settings import CROP_ORIENTATION, WATERMARK, WATERMARK_POSITION, PUT_WATERMARK, DEFAULT_EXTENSION
from django.conf import settings
import os
import time
from hashlib import md5
from random import randint

def crop_resized(image, size):
    """
    # target shape (landscape or portrait)
    target_s = "portrait" if size[0] < size[1] else "landscape"
    
    # source shape (width or height)
    source_s = "portrait" if image.size[0] < image.size[1] else "landscape"
    
    if target_s == "landscape":
        ratio = size[0] / float(image.size[0])
    else:
        ratio = size[1] / float(image.size[1])
        
    new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
    
    new_image = image.resize(new_size, Image.ANTIALIAS)
    
    box = [0, 0, new_image.size[0], new_image.size[1]]
    if CROP_ORIENTATION == "center":
        if target_s == source_s == "portrait" or source_s != target_s == "portrait":
            #will cut up and down edges
            distance = (new_image.size[0] - size[0]) / 2
            box[0] += distance
            box[2] -= distance
        elif target_s == source_s == "landscape" or source_s != target_s == "landscape":
            #will cut right and left edges
            distance = (new_image.size[1] - size[1]) / 2
            box[1] += distance
            box[3] -= distance
    
    box = tuple(box)
    
    new_image = new_image.crop(box)
    return new_image
    """
    return ImageOps.fit(image, size, Image.ANTIALIAS, (0.5, 0.5))

def put_watermark(image, watermark_file=None, border=10, position=None):
    if position:
        pos = position
    else:
        pos = WATERMARK_POSITION
    
    if watermark_file:
        watermark = Image.open(watermark_file)
    else:
        watermark = Image.open(WATERMARK)
    
    box = [0, 0, watermark.size[0], watermark.size[1]]
    
    if pos == "bottomleft":
        box = [
            border,
            image.size[1] - watermark.size[1] - border,
            watermark.size[0] + border,
            image.size[1] - border
        ]
    elif pos == "bottomright":
        box = [
            image.size[0] - watermark.size[0] - border,
            image.size[1] - watermark.size[1] - border,
            image.size[0] - border,
            image.size[1] - border
        ]
    elif pos == "topleft":
        box = [
            border,
            border,
            watermark.size[0] + border,
            watermark.size[1] + border
        ]
    elif pos == "topright":
        box = [
            image.size[0] - watermark.size[0] - border,
            border,
            image.size[0] - border,
            watermark.size[1] + border
        ]
        
    image = image.convert('RGBA')
    watermark = watermark.convert('RGBA')
    r, g, b, a = watermark.split()
    image.paste(watermark, box, mask=a)
    
    return image


def set_image_path(instance, filename):
    if hasattr(instance, 'album'):
        path = "albums/%d/" % instance.album.id
    else:
        path = "albums/covers/"
    #path = settings.MEDIA_ROOT + path
    if not os.path.exists(settings.MEDIA_ROOT + path):
        os.makedirs(settings.MEDIA_ROOT + path)
    timestamp = int(time.time())
    base_path = path
    while True:
        timestamp += 1
        string = (randint(0, 100), timestamp)
        path = base_path + md5("%d--%d" % string).hexdigest() + (".%s" % DEFAULT_EXTENSION)
        if not os.path.exists(settings.MEDIA_ROOT + path):
            break
    return path
