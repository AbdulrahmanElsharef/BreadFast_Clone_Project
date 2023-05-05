from django.contrib import admin
from .models import Department, Product, ProductImage, ProductReview
# Register your models here.


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage


# class ProductReviewInline(admin.TabularInline):
#     model = ProductReview


# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImage, ProductReview]


admin.site.register(Department)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
