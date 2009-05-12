# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from webalbum.models import Picture
from webalbum.settings import IMAGE_SIZE
from PIL import Image, ImageOps
from StringIO import StringIO

def fit(request, id, width=None, height=None):
    picture = get_object_or_404(Picture, pk=id)
    if width and height:
        size = (int(width), int(height))
    else: 
        size = IMAGE_SIZE
    im = Image.open(picture.image.path)
    im = ImageOps.fit(im, size, Image.ANTIALIAS)
    f = StringIO()
    im.save(f, "JPEG")
    return HttpResponse(f.getvalue(), mimetype="image/jpeg")
