from django.contrib import admin
from .models import Category, Product, ProductImage, Size, Colour


admin.site.site_header = "AMLO Shoe Store"
admin.site.site_title = "AMLO Admin"
admin.site.index_title = "AMLO Store Management"


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class SizeInline(admin.TabularInline):
    model = Size
    extra = 1


class ColourInline(admin.TabularInline):
    model = Colour
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "price",
        "available",
        "featured",
        "new_arrival"
    ]

    list_filter = [
        "category",
        "available",
        "featured",
        "new_arrival"
    ]

    list_editable = [
        "price",
        "available",
        "featured",
        "new_arrival"
    ]

    search_fields = [
        "name",
        "description"
    ]

    prepopulated_fields = {
        "slug": ("name",)
    }

    inlines = [
        ProductImageInline,
        SizeInline,
        ColourInline
    ]