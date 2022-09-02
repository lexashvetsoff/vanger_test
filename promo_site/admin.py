from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from promo_site.models import Slider, SliderImage


class SliderImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SliderImage
    fields = ['image']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


@admin.register(Slider)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [SliderImageInline]


admin.site.site_title = 'Django Nasa'
admin.site.site_header = 'Django Nasa'
