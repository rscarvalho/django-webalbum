from django import forms
from webalbum.models import Album, Picture
from webalbum.utils import set_image_path
from webalbum import settings as web_settings
from django.utils.translation import ugettext as _
from django.forms.util import ErrorList
from zipfile import ZipFile, is_zipfile
from tempfile import mkdtemp, mkstemp
import os
from django.conf import settings


class AlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        if web_settings.HAS_HIGHLIGHT:
            self.fields['highlight'].required = True
            
        if web_settings.HAS_PHOTOGRAPHER:
            self.fields['photographer'].required = True
    
    class Meta:
        model = Album



class AddPhotoForm(forms.Form):
    album = forms.ModelChoiceField(queryset=Album.objects.order_by("-pub_date"))
    images = forms.FileField(help_text=_("A .zip files containing pictures"), required=True)
    
    def clean_images(self):
        cleaned_data = self.cleaned_data
        album = cleaned_data['album']
        
        if cleaned_data.get("images"):
            zhandler, zfile = mkstemp(suffix=cleaned_data['images'].name)
            zhandler = open(zfile, 'wb')
            zhandler.write(cleaned_data['images'].read())
            zhandler.flush()
            errors = []
            if zfile.lower().endswith('.zip') and is_zipfile(zfile):
                zf = ZipFile(zfile, 'r')
                imported_files = 0
                error_files = 0
                for zname in zf.namelist():
                    if not zname.lower().endswith(".jpg"): continue
                    pct = Picture(album=album)
                    picture_path = set_image_path(pct, zname)
                    full_path = settings.MEDIA_ROOT + picture_path
                    fh = open(full_path, 'wb')
                    fh.write(zf.read(zname))
                    fh.flush()
                    fh.close()
                    #save image
                    pct.image = picture_path
                    try:
                        pct.save()
                        imported_files += 1
                    except Exception, ex:
                        imported_files -= 1
                        error_files += 1
                        errors.append(str(ex))
                        #raise ex
                    fh.close()
                    
                self.cleaned_data['imported_files'] = imported_files
                self.cleaned_data['error_files'] = error_files
                #cleanup
                zf.close()
                os.remove(zfile)
            else:
                #print zfile
                errors.append(_("Invalid file format. It must be a .zip file"))
                
            if errors:
                self._errors['images'] = ErrorList(errors)
        
        return cleaned_data['images']

