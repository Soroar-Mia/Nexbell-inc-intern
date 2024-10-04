from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') 
    search_fields = ('name',)              


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')  
    search_fields = ('name', 'category__name') 
    list_filter = ('category',)                
    list_editable = ('price',)                 
    ordering = ('category', 'name') 


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
