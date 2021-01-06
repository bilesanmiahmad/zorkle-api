from django.contrib import admin
from .models import Clothes, Footwear, Accessory, Batch

# Register your models here.

class FootwearModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'design_name',
        'product_number',
        'gender',
        'color',
        'batch',
        'size',
        'category',
        'quantity_in_stock',
        'unit_price',
        'selling_price'
    )
    list_filter = ('gender', 'design_name', 'color', 'size')
    search_fields = ('design_name', 'product_number')


class AccessoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'design_name',
        'product_number',
        'gender',
        'color',
        'batch',
        'category',
        'quantity_in_stock',
        'unit_price',
        'selling_price'
    )
    list_filter = ('gender', 'design_name', 'color')
    search_fields = ('design_name', 'product_number')


class ClothesModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'design_name',
        'product_number',
        'gender',
        'color',
        'batch',
        'size',
        'category',
        'quantity_in_stock',
        'unit_price',
        'selling_price'
    )
    list_filter = ('gender', 'design_name', 'color', 'size')
    search_fields = ('design_name', 'product_number')

admin.site.register(Batch)
admin.site.register(Footwear, FootwearModelAdmin)
admin.site.register(Accessory, AccessoryModelAdmin)
admin.site.register(Clothes, ClothesModelAdmin)

admin.site.site_header = "Zorkle Admin"
admin.site.site_title = "Zorkle Admin Portal"
admin.site.index_title = "Welcome to Zorkle Portal"