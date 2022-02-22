from typing import Dict, Callable

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from banners_app.services import banner
from goods_app.forms import ReviewForm
from goods_app.models import Product
from goods_app.services import get_reviews, calculate_product_rating, context_pagination


class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs) -> Dict:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banners'] = banner()
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'goods_app/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs) -> Dict:
        context = super().get_context_data(**kwargs)
        reviews = get_reviews(product=context['product'])
        context['reviews_count'] = reviews.count
        context['comments'] = context_pagination(request=self.request, queryset=reviews)
        context['form'] = ReviewForm()
        return context

    @login_required
    def post(self, request, slug: str) -> Callable:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            calculate_product_rating(product=self.get_object())
            return redirect(reverse('goods-polls:product-detail', kwargs={'slug': slug}))
        context = dict()
        context['form'] = ReviewForm()
        context['product'] = self.get_object()
        reviews = get_reviews(context['product'])
        context['reviews_count'] = reviews.count
        context['comments'] = context_pagination(request=request, queryset=reviews)
        return render(request, 'goods_app/product_detail.html', context=context)
