#!/bin/bash
python manage.py makemigrations --no-input
python manage.py migrate  --no-input

python manage.py loaddata fixtures/goods_app.product_category.json
python manage.py loaddata fixtures/profiles_app_groups.json
python manage.py loaddata fixtures/goods_app.product.json
python manage.py loaddata fixtures/profiles_app.users.json
python manage.py loaddata fixtures/stores_app._seller.json
python manage.py loaddata fixtures/discounts_app.cartdiscount.json
python manage.py loaddata fixtures/goods_app.specificationnames.json
python manage.py loaddata fixtures/profiles_app_social.json
python manage.py loaddata fixtures/discounts_app.groupdiscount.json
python manage.py loaddata fixtures/orders_app.order.json
python manage.py loaddata fixtures/stores_app.sellerproduct.json
python manage.py loaddata fixtures/discounts_app.productdiscount.json
python manage.py loaddata fixtures/banners_app.banners.json
python manage.py loaddata fixtures/orders_app.orderproduct.json

python manage.py collectstatic --no-input
python manage.py compilemessages
python manage.py runserver 0.0.0.0:8000
