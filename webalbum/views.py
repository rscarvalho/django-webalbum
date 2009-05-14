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
