from django.contrib import admin
from .models import Category, Product

# Register Category model with customization
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the admin list view
    search_fields = ('name',)               # Add search capability for 'name' field

# Register Product model with customization
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')  # Display these fields in the admin list view
    search_fields = ('name', 'category__name')  # Add search capability for 'name' and 'category' fields
    list_filter = ('category',)                 # Add filter by category in the admin list view
    list_editable = ('price',)                  # Allow price to be edited directly in the list view
    ordering = ('category', 'name')             # Sort by category and then by product name

# Register the models with admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
