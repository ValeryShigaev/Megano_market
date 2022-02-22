from django.contrib import admin
from goods_app.models import ProductCategory, Product, ProductComment, Specifications, SpecificationsNames


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class SpecificationsAdmin(admin.TabularInline):
    model = Specifications

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category')
    list_filter = ('name', 'code', 'category')
    search_fields = ('name', 'code', 'category')
    prepopulated_fields = {'slug': ('name', 'category')}

    inlines = [SpecificationsAdmin]


@admin.register(ProductComment)
class ProductComment(admin.ModelAdmin):
    list_display = ('author', 'content', 'added')
    list_filter = ('author', 'added')
    search_fields = ('author', 'added')


@admin.register(Specifications)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('value',)

@admin.register(SpecificationsNames)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name',)
