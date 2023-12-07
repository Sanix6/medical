from django.contrib import admin
from .models import *


admin.site.register(Direction)
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_activate",
    )
    list_display_links = ("title",)
    list_editable = ("is_activate",)


@admin.register(Gallery)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'year')
    search_fields = ['year']
