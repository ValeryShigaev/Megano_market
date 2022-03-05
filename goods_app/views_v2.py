from decimal import Decimal
from typing import Dict

from django.db.models import QuerySet, Q
from django.http import JsonResponse
from django.views.generic import ListView
from taggit.models import Tag

from goods_app.models import ProductCategory
from stores_app.models import SellerProduct, Seller


class GoodsMixin:

    @classmethod
    def get_products(cls, **kwargs) -> QuerySet:
        if 'category_id' in kwargs.keys():
            return SellerProduct.objects.select_related('product', 'discount', 'seller')\
                                        .prefetch_related('product__category')\
                                        .filter(category=kwargs.get('category_id'))
        elif 'instance' in kwargs.keys():
            return SellerProduct.objects.select_related('product', 'discount', 'seller')\
                                        .prefetch_related('product__category')\
                                        .filter(seller_products__seller=kwargs.get('instance'))
        else:
            return SellerProduct.objects.select_related('product', 'discount', 'seller')\
                                        .prefetch_related('product__category').all()

    def get_shops(self):
        return Seller.objects.all()

    def get_tags(self):
        return Tag.objects.all()

    def get_categories(self):
        return ProductCategory.objects.all()

    def get_catalog_products(self):
        pass


class CatalogView(GoodsMixin, ListView):
    """
    Базовое View для фильтрации продуктов с помощью ProductFilterView или JsonFilterStoreView
    """
    model = SellerProduct
    context_object_name = 'products'
    template_name = 'goods_app/test-catalog.html'

    def get_queryset(self) -> QuerySet:
        return self.get_products()

    def get_context_data(self, *args, **kwargs) -> Dict:
        context = super().get_context_data(*args, **kwargs)
        context['sellers'] = self.get_shops()
        context['categories'] = self.get_categories()
        context['tags'] = self.get_tags()
        return context


class JsonFilterStore(ListView):
    """
    Фильтр с использованием jquery, ajax и hogan для частичного обновления страницы.
    """
    def get_queryset(self) -> QuerySet:
        price = self.request.GET.get('price').split(';')
        price_min = Decimal(price[0])
        price_max = Decimal(price[1])
        if self.request.GET.get('in_stock') == 'on':
            stock = 1
        else:
            stock = 0
        queryset = SellerProduct.objects.select_related('product', 'seller', 'discount')\
                                        .prefetch_related('product__category')\
                                        .filter(seller__name__icontains=self.request.GET.get('seller', ""),
                                                product__name__icontains=self.request.GET.get('title', ""),
                                                product__category__name__icontains=self.request.GET.get('category', ""),
                                                price_after_discount__range=(price_min, price_max),
                                                quantity__gte=stock)\
                                        .values('id','product__category', 'product__name',
                                                'product__category__name', 'product__slug',
                                                'discount__percent', 'discount__amount',
                                                'price', 'price_after_discount')

        print(list(queryset)[0])
        return queryset

    def get(self, request, *args, **kwargs) -> JsonResponse:
        queryset = self.get_queryset()
        return JsonResponse({'products': list(queryset)}, safe=False)