from django.contrib import admin
from webalbum.models import Album, Picture
from webalbum.forms import AddPhotoForm, AlbumForm
from webalbum import settings as web_settings
from django.conf.urls.defaults import patterns
from django import template
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django import template
from django.http import HttpResponseRedirect

exclude_fields = []
if not web_settings.HAS_PHOTOGRAPHER:
    exclude_fields.append("photographer")
if not web_settings.HAS_HIGHLIGHT:
    exclude_fields.append("highlight")


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "pub_date", "active")
    list_filter = ("pub_date",)
    search_fields = ("name", )
    form = AlbumForm
    exclude = tuple(exclude_fields)
    
    def __call__(self, request, url):
        if url == "add_photos" and request.user.is_authenticated() and request.user.is_staff:
            return self.add_photos(request)
        return super(AlbumAdmin, self).__call__(request, url)
        
    def add_photos(self, request):
        if request.POST:
            form = AddPhotoForm(request.POST, request.FILES)
        else:
            form = AddPhotoForm()
            
        if form.is_valid():
            message = _("Photos were processed. %(imported_files)d photos were processed successfully. %(error_files)d photos were not processed") % \
                        dict(imported_files=form.cleaned_data.get('imported_files', 0), error_files=form.cleaned_data.get('error_files', 0))
            request.user.message_set.create(message=message)
            return HttpResponseRedirect("../")
            #print form.cleaned_data
        
        context = template.RequestContext(request, {
            'title': _("Add photos"),
            'opts': Album._meta,
            'form': form,
            'app_label': _('webalbum'),
            'change': True,
            'is_popup': request.GET.get('_popup', False),
            'save_as': False,
            'has_delete_permission': True,
            'has_add_permission': True,
            'has_change_permission': True
        })
        return render_to_response("admin/webalbum/album/add_photos.html", context_instance=context)
    
    
class PictureAdmin(admin.ModelAdmin):
    list_filter = ("album",)
    list_display = ("image", "album")
    search_fields = ("image",)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Picture, PictureAdmin)
