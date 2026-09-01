from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Category


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
          return ["home", "contact", "size_guide"]

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.all().order_by("id")

    def location(self, obj):
        return reverse(
            "category_products",
            kwargs={"slug": obj.slug}
        )


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.filter(
            available=True
        ).order_by("id")

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/product/{obj.slug}/"