# Generated by Django 4.0.1 on 2022-02-08 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_app', '0004_alter_product_options_alter_product_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='product_image'),
        ),
    ]
