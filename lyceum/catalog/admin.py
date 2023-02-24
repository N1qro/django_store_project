import catalog.models
from django.contrib import admin


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )

    list_editable = ("is_published",)
    list_display_links = ("name",)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",

    )
