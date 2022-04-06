from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from discounts_app.models import ProductDiscount, GroupDiscount, CartDiscount


@receiver(post_save, sender=ProductDiscount)
def product_discount_reset_cache_save_handler(sender, **kwargs) -> None:
    """
    Signal for clearing cache
    """
    user_id = kwargs['instance'].seller.owner_id
    cache.delete('owner_product_discounts:{}'.format(user_id))


@receiver(post_delete, sender=ProductDiscount)
def product_discount_cache_del_handler(sender, **kwargs) -> None:
    """
    Signal for clearing cache
    """
    user_id = kwargs['instance'].seller.owner_id
    cache.delete('owner_product_discounts:{}'.format(user_id))


@receiver(post_save, sender=GroupDiscount)
def group_discounts_reset_cache_save_handler(sender, **kwargs) -> None:
    """
    Signal for clearing cache
    """
    user_id = kwargs['instance'].seller.owner_id
    cache.delete('owner_product_discounts:{}'.format(user_id))


@receiver(post_delete, sender=GroupDiscount)
def group_discounts_cache_del_handler(sender, **kwargs) -> None:
    """
    Signal for clearing cache
    """
    user_id = kwargs['instance'].seller.owner_id
    cache.delete('owner_product_discounts:{}'.format(user_id))


@receiver(post_save, sender=CartDiscount)
def cart_discounts_reset_cache_save_handler(sender, **kwargs) -> None:
    """
    Signal for clearing cache
    """
    user_id = kwargs['instance'].seller.owner_id
    cache.delete('owner_product_discounts:{}'.format(user_id))


@receiver(post_delete, sender=CartDiscount)
def cart_discounts_cache_del_handler(sender, **kwargs) -> None:
    """
    Signal for clearing cache
    """
    user_id = kwargs['instance'].seller.owner_id
    cache.delete('owner_product_discounts:{}'.format(user_id))
