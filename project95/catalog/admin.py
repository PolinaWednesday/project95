from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_title', 'product_price', 'product_category', 'in_stock', 'owner', 'is_published')
    list_filter = ('in_stock', 'product_category',)
    search_fields = ('product_name', 'product_title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_active',)
    list_filter = ('is_active', 'product',)
    search_fields = ('product', 'version_name',)
