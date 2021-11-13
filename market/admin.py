from django.contrib import admin

from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'rating', 'image', 'get_small_image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "get_small_image")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("provider", "product", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("consumer", "created_at", "updated_at", "status")


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("product", "order", "amount")