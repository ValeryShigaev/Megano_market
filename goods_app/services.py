from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Avg, QuerySet
from goods_app.models import Product, ProductComment


def calculate_product_rating(product: 'Product') -> None:
    rating = ProductComment.objects.only('rating').filter(product_id=product.id).aggregate(Avg('rating'))['rating__avg']
    if rating:
        product.rating = round(float(rating), 0)
        product.save(update_fields=['rating'])


def get_reviews(product: 'Product') -> QuerySet:
    reviews_cache_key = 'reviews:{}'.format(product.id)
    reviews = cache.get(reviews_cache_key)
    if not reviews:
        reviews = product.product_comments.all().order_by('-id')
        cache.set(reviews_cache_key, reviews, 60 * 60)
    return reviews


def context_pagination(request, queryset: QuerySet, size_page: int = 3) -> Paginator:
    """
    Функция для создания пагинации
    :return: Paginator
    """
    paginator = Paginator(object_list=queryset, per_page=size_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(number=page_number)
    return page_obj

