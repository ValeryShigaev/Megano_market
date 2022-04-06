from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from goods_app.models import ProductCategory, Product, ProductComment, Specifications, SpecificationsNames
from settings_app.forms import CheckImageForm, CheckImageIconForm


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    form = CheckImageIconForm
    list_display = ('get_icon', 'name', 'parent', 'image')
    list_display_links = ('get_icon', 'name')
    list_filter = ('name',)
    readonly_fields = ('get_icon',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',), }

    def get_icon(self, obj):
        return mark_safe(f'<img src="{obj.icon.url}" width="20" height="20">')

    get_icon.short_description = _('icon')


class SpecificationsInline(admin.TabularInline):
    model = Specifications


class CommentsInline(admin.TabularInline):
    model = ProductComment
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = CheckImageForm
    list_display = ('get_image', 'name', 'category', 'is_published', 'limited', 'get_tags')
    list_display_links = ('get_image', 'name')
    list_filter = ('category', 'is_published', 'tags', 'limited')
    readonly_fields = ('get_image',)
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name', 'code'),
                           'tags': ('category', )}

    inlines = [SpecificationsInline, CommentsInline]

    actions = ['mark_published', 'mark_unpublished']

    def get_tags(self, obj):
        lst_tags = []
        for item in obj.tags.all().values('name'):
            lst_tags.append(str(item['name']))
        return ", ".join(lst_tags)

    def mark_published(self, request: HttpRequest, queryset: QuerySet) -> None:
        queryset.update(is_published=True)

    def mark_unpublished(self, request: HttpRequest, queryset: QuerySet) -> None:
        queryset.update(is_published=False)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="60" height="60">')

    mark_published.short_description = _('Publish')
    mark_unpublished.short_description = _('Remove from publication')

    get_image.short_description = _('image')
    get_tags.short_description = _('tags')


@admin.register(ProductComment)
class ProductComment(admin.ModelAdmin):
    list_display = ('author', 'get_text_comment', 'added')
    list_filter = ('author', 'added')
    search_fields = ('author', 'added')

    actions = ['delete_text']

    def delete_text(self, request, queryset):
        queryset.update(text_comment=_('[removed by admin]'))

    def get_text_comment(self, obj):
        return ''.join([obj.text_comment[:15], "..."])

    get_text_comment.short_description = _('text comment')
    delete_text.short_description = _('delete text comment')


@admin.register(Specifications)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('current_specification', 'value', 'product')
    list_filter = ('product', )
    search_fields = ('current_specification', 'value', 'product')


@admin.register(SpecificationsNames)
class SpecificationNamesAdmin(admin.ModelAdmin):
    list_display = ('name', )
