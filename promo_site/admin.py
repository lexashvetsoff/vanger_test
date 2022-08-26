from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from promo_site.models import Slider, SliderImage


class SliderImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SliderImage
    readonly_fields = ['get_preview_image']
    fields = ['image', 'get_preview_image']
    # fields = ['image']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
    
    def get_preview_image(self, obj):
        print(format_html('<img src="{}" style="max-height: 200px;"/>', obj.image.url))   
        return format_html('<img src="{}" style="max-height: 200px;"/>', obj.image.url)
    
    get_preview_image.short_description = 'Превью'


@admin.register(Slider)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [SliderImageInline]


admin.site.site_title = 'Django Nasa'
admin.site.site_header = 'Django Nasa'

# admin.site.register(Slider)
# admin.site.register(SliderImage)
