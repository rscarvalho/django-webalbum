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
