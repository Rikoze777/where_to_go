from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    raw_id_fields = ('place', )
    readonly_fields = ["place_image", ]

    def place_image(self, obj):
        return format_html("<img src={} style='max-height:{};\
                           max-width:{};height:{};width:{};'/>",
                           obj.img.url, "200px", "200px",
                           "auto", "auto")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin,):
    list_display = ['img']
