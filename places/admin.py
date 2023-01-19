from django.contrib import admin
from places.models import Place, Image
from django.utils.safestring import mark_safe


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ('place', )
    readonly_fields = ["place_image"]

    def place_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.img.url,
            width=obj.img.width,
            height=obj.img.height,
            )
    )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin,):
    list_display = ['img']
