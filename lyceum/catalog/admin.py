from django.contrib import admin

import catalog.models
from .models import Item, ItemPicture


class ItemPictureInline(admin.TabularInline):
    model = ItemPicture
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)

    inlines = [ItemPictureInline, ]

    # fieldsets = (
    #     (_('Main'), {
    #         'fields': ('name', 'text', 'category', 'tags', 'main_picture')
    #     }),
    #     (_('Advanced options'), {
    #         'fields': ('is_published',),
    #         'classes': ('collapse',)
    #     }),
    # )


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Category.name.field.name,
    )
    list_display_links = ("name",)


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.name.field.name,
    )
    list_display_links = ("name",)
