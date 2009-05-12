from django.db import models
from django.utils.translation import ugettext as _, ngettext
from django.conf import settings
import time
from webalbum import settings as web_settings
from webalbum.utils import crop_resized, put_watermark, set_image_path
from PIL import Image, ImageOps
import os
import re

class Album(models.Model):
    name = models.CharField(_("name"), max_length=200)
    description = models.TextField(_("description"), blank=True)
    photographer = models.CharField(_("photographer"), blank=True, null=True, max_length=100)
    pub_date = models.DateField(_("publish date"))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(_("cover image"), upload_to=set_image_path)
    highlight = models.ImageField(_("highlight image"), upload_to=set_image_path, 
                                  blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)
    
    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "name"]
        verbose_name = ngettext("Album", "Albums", 1)
        verbose_name_plural = ngettext("Album", "Albums", 2)
    
    def __unicode__(self):
        return "%s - (%s)" % (self.name, self.pub_date.strftime("%d/%m/%Y"))
    
    @property
    def highlight_thumb(self):
        return "%s_thumb.%s" % tuple(self.highlight.url.rsplit(".", 1))
        
    @property
    def highlight_thumb_path(self):
        return "%s_thumb.%s" % tuple(self.highlight.path.rsplit(".", 1))
        
    @property
    def cover_thumb_path(self):
        return "%s_thumb.%s" % tuple(self.image.path.rsplit(".", 1))
        
    @property
    def cover_thumb(self):
        return "%s_thumb.%s" % tuple(self.image.url.rsplit(".", 1))
    
    def save(self, force_insert=False, force_update=False):
        im = Image.open(self.image.path)
        if im.size != web_settings.COVER_SIZE:
            im = ImageOps.fit(im, web_settings.COVER_SIZE, Image.ANTIALIAS)
            if web_settings.OVER_COVER:
                im = put_watermark(im, web_settings.OVER_COVER, 0, "topleft")
            im.save(self.image.path, quality=100, optimize=0)
        if web_settings.COVER_THUMB_SIZE:
            thumb = ImageOps.fit(im, web_settings.COVER_THUMB_SIZE, Image.ANTIALIAS)
            thumb.save(self.cover_thumb_path, quality=100)
            
        if web_settings.HAS_HIGHLIGHT:
            im = Image.open(self.highlight.path)
            if not os.path.exists(self.highlight_thumb_path):
                thumb = ImageOps.fit(im, web_settings.HIGHLIGHT_THUMB_SIZE, Image.ANTIALIAS)
                thumb.save(self.highlight_thumb_path, quality=100)
            if im.size != web_settings.HIGHLIGHT_SIZE:
                im = ImageOps.fit(im, web_settings.HIGHLIGHT_SIZE, Image.ANTIALIAS)
            
            if web_settings.HIGHLIGHT_WATERMARK:
                im = put_watermark(im, web_settings.HIGHLIGHT_WATERMARK, 0, 
                                   web_settings.HIGHLIGHT_WATERMARK_POSITION)
                
            im.save(self.highlight.path, quality=100, optimize=0)
            
        super(Album, self).save(force_insert, force_update)
        
    def delete(self):
        if web_settings.HAS_HIGHLIGHT:
            if os.path.exists(self.highlight_thumb_path):
                os.remove(self.highlight_thumb_path)
        if os.path.exists(self.cover_thumb_path):
            os.remove(self.cover_thumb_path)
        super(Album, self).delete()
    

class Picture(models.Model):
    image = models.ImageField(_("Image"), upload_to=set_image_path)
    width = models.IntegerField(editable=False, default=0)
    height = models.IntegerField(editable=False, default=0)
    album = models.ForeignKey(Album)
    
    class Meta:
        verbose_name = ngettext("Picture", "Pictures", 1)
        verbose_name_plural = ngettext("Picture", "Pictures", 2)
    
    def resize_and_crop(self):
        # if not self.image:
        #             im = Image.open(self.image.file)
        #             size = (web_settings.IMAGE_WIDTH, web_settings.IMAGE_HEIGHT)
        #             im = ImageOps.fit(im, size, Image.ANTIALIAS)
        #             im.save(self.image.path)
        
        try:
            im = Image.open(self.image.path)
        except IOError, e:
            self.delete()
            return
            #raise Exception, str(e) + " :: " + self.image.path
        
        if web_settings.PORTRAIT_SIZE and im.size[0] < im.size[1]:
            im = ImageOps.fit(im, web_settings.PORTRAIT_SIZE, Image.ANTIALIAS)
        else:
            im = ImageOps.fit(im, web_settings.IMAGE_SIZE, Image.ANTIALIAS)
                              
        thumb = ImageOps.fit(im, web_settings.PHOTO_THUMBNAIL_SIZE, Image.ANTIALIAS)
        thumb.save(self.thumbnail_path)
        if web_settings.PUT_WATERMARK:
            im = put_watermark(im)
        im.save(self.image.path, im.format, quality=90)
    
    @property
    def thumbnail_path(self):
        return "%s_thumb.%s" % tuple(self.image.path.rsplit(".", 1))
    
    @property
    def thumbnail(self):
        return "%s_thumb.%s" % tuple(self.image.url.rsplit(".", 1))
    
    def save(self, force_insert=False, force_update=False):
        #_id = None if self.id is None else self.id
        _id = self.id
        
        super(Picture, self).save(force_insert, force_update)
        
        if _id is None:
            self.resize_and_crop()
            
    def delete(self):
        if os.path.exists(self.thumbnail_path):
            os.remove(self.thumbnail_path)
        super(Picture, self).delete()
    
    def __unicode__(self):
        #return self.image.name if self.image else "--undefined--"
        try:
            return self.image.name
        except:
            return "--undefined--"
