from django.contrib import admin


from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','quantity']
    fields = ['name', 'description', ('price','quantity'), 'category']
    readonly_fields = ['description']
    ordering = ['name']
    search_fields = ['name']


# Register your models here.
